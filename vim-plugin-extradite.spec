%define		plugin	extradite
%define		snap	20190907
Summary:	Vim plugin: A git commit browser
Name:		vim-plugin-%{plugin}
Version:	1.1
Release:	0.%{snap}.1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	vim-extradite-%{snap}.tar.gz
# Source0-md5:	cd80ddb0a20f4171767956ca722a422a
URL:		http://int3.github.io/vim-extradite/
Requires:	vim-plugin-fugitive
Requires:	vim-rt >= 4:7.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
A git commit browser.

%package doc
Summary:	Documentation for extradite Vim plugin
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:7.4.2054-2

%description doc
Documentation for extradite Vim plugin.

%prep
%setup -qn vim-extradite

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/
cp -pr doc plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%doc README.markdown
%{_vimdatadir}/plugin/extradite.vim

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/extradite.txt
