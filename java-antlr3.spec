# TODO:
# - Shell wrapper
# - Some docs?

# NOTE:
# - It is not just a new version of antlr, so it must not conflict with antlr-2
# - No, we can not build it from sources. It requires fuckin maven.

#
# Conditional build:
%bcond_without	ant		# don't build ant task


%define		srcname antlr3
Summary:	ANother Tool for Language Recognition
Summary(pl.UTF-8):	ANother Tool for Language Recognition - analizator językowy
Name:		java-antlr3
Version:	3.2
Release:	3
License:	Public Domain
Group:		Development/Languages/Java
Source0:	http://antlr3.org/download/antlr-%{version}.jar
# From http://antlr.org/share/1169924912745/antlr3-task.zip
Source1:	ANTLR3.java
Source2:	antlib.xml
# Source0-md5:	ee7dc3fb20cf3e9efd871e297c0d532b
URL:		http://antlr3.org/
%if %{with ant}
BuildRequires:	ant
BuildRequires:	jdk
%endif
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Obsoletes:	antlr3 < %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ANTLR, ANother Tool for Language Recognition, is a language tool that
provides a framework for constructing recognizers, interpreters,
compilers, and translators from grammatical descriptions containing
actions in a variety of target languages. ANTLR provides excellent
support for tree construction, tree walking, translation, error
recovery, and error reporting.

%description -l pl.UTF-8
ANTLR (ANother Tool for Language Recognition - jeszcze jedno narzędzie
do rozpoznawania języka) to narzędzie językowe, udostępniające
szkielet do tworzenia analizatorów, interpreterów, kompilatorów oraz
translatorów z opisów gramatycznych zawierających akcje dla rozmaitych
języków docelowych. ANTLR zapewnia dobre wsparcie przy konstrukcji
drzewa, przechodzeniu drzewa, translacji, powrocie ze stanów błędnych
oraz zgłaszaniu błędów.

%package -n ant-antlr3
Summary:	Antlr3 task for ant
Summary(pl.UTF-8):	Zadanie antlr3 dla anta
License:	Apache v2
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description -n ant-antlr3
Ant task for antlr3.

%description -n ant-antlr3 -l pl.UTF-8

%prep
%if %{with ant}
%setup -q -T -c
mkdir -p org/apache/tools/ant/antlr
mkdir build
cp %{SOURCE1} org/apache/tools/ant/antlr
cp %{SOURCE2} org/apache/tools/ant/antlr

%build
CLASSPATH=$(find-jar ant):%{SOURCE0}
export CLASSPATH
export LC_ALL=en_US

javac -d build org/apache/tools/ant/antlr/*java
cp org/apache/tools/ant/antlr/antlib.xml build/org/apache/tools/ant/antlr/antlib.xml

jar cf ant-antlr3.jar -C build org
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}/ant

# jars
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -sf %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%if %{with ant}
cp -a ant-antlr3.jar $RPM_BUILD_ROOT%{_javadir}/ant/ant-antlr3.jar
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/antlr3-%{version}.jar
%{_javadir}/antlr3.jar

%if %{with ant}
%files -n ant-antlr3
%defattr(644,root,root,755)
%{_javadir}/ant/ant-antlr3.jar
%endif
