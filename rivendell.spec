Name:	    Rivendell	
Version:	2
Release:	1
Summary:	The "Rivendell" radio automation program from http://www.rivendellaudio.org/

Group:		
License:	GPL v3
URL:		www.rivendellaudio.org/ftpdocs/rivendell/
Source0:	www.rivendellaudio.org/ftpdocs/rivendell/rivendell-2.9.2.tar.gz

BuildRequires:	Apache Web Server, Cdda2Wav, ID3Lib, LibCurl, LibParanoia, LibSndFile,mySQL Database Server, PAM Pluggable Authentication Modules, OggVorbis, Qt Toolkit, Secret Rabbit Code, SoundTouch Audio Processing Library, X11 Window System

%description
The Rivendell radio automation program, available in all it's glory, 
in a neat little package for fedora workstations and virtual 
machines everywhere.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog

