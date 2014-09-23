Name:	    Rivendell	
Version:	2
Release:	1
Summary:	The "Rivendell" radio automation program from http://www.rivendellaudio.org/

Group:		
License:	GPL v3
URL:		www.rivendellaudio.org/ftpdocs/rivendell/
Source0:	www.rivendellaudio.org/ftpdocs/rivendell/rivendell-2.9.2.tar.gz

Requires:	Apache Web Server, Cdda2Wav, ID3Lib, LibCurl, LibParanoia, LibSndFile,mySQL Database Server, PAM Pluggable Authentication Modules, OggVorbis, Qt Toolkit, Secret Rabbit Code, SoundTouch Audio Processing Library, X11 Window System

BuildRequires: gcc-4.8.3-1.fc20.x86_64, libgcc-4.8.3-1.fc20.x86_64, gcc-gfortran-4.8.3-1.fc20.x86_64, gcc-c++-4.8.3-1.fc20.x86_64, qt-4.8.6-10.fc20.x86_64, qt-devel-4.8.6-10.fc20.x86_64, qt-x11-4.8.6-10.fc20.x86_64, qt-mobility-4.8.6-10.fc20.x86_64

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

