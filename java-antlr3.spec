# TODO:
# - Shell wrapper
# - Some docs?

# NOTE:
# - It is not just a new version of antlr, so it must not conflicts with antlr-2
# - No, we can not build it from sources. It requires fuckin maven.

%include	/usr/lib/rpm/macros.java
Summary:	ANother Tool for Language Recognition
Name:		antlr3
Version:	3.2
Release:	0.1
License:	Public Domain
Group:		Libraries/Java
Source0:	http://antlr.org/download/antlr-3.2.jar
# Source0-md5:	ee7dc3fb20cf3e9efd871e297c0d532b
URL:		http://antlr.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ANTLR, ANother Tool for Language Recognition, is a language tool that provides
a framework for constructing recognizers, interpreters, compilers, and
translators from grammatical descriptions containing actions in a variety of
target languages. ANTLR provides excellent support for tree construction, tree
walking, translation, error recovery, and error reporting.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar
