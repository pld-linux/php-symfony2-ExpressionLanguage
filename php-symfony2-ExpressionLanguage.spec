%define		package	ExpressionLanguage
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 ExpressionLanguage Component
Name:		php-symfony2-ExpressionLanguage
Version:	2.7.7
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/expression-language/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	7f9e69058a5950760395c09789e98fe2
URL:		http://symfony.com/doc/2.7/components/expression_language/index.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(pcre)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony2 ExpressionLanguage Component.

The ExpressionLanguage component provides an engine that can compile
and evaluate expressions. An expression is a one-liner that returns a
value (mostly, but not limited to, Booleans).

%prep
%setup -q -n expression-language-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests
# dev
rm $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Resources/bin/generate_operator_regex.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/ExpressionLanguage
%{php_data_dir}/Symfony/Component/ExpressionLanguage/*.php
%{php_data_dir}/Symfony/Component/ExpressionLanguage/Node
%{php_data_dir}/Symfony/Component/ExpressionLanguage/ParserCache
