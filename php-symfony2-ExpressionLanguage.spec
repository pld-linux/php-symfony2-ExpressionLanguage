%define		pearname	ExpressionLanguage
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 ExpressionLanguage Component
Name:		php-symfony2-ExpressionLanguage
Version:	2.4.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	113788162b69ea7383ea08342ba48e75
URL:		http://symfony.com/doc/2.4/components/expression_language/index.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony2 ExpressionLanguage Component.

The ExpressionLanguage component provides an engine that can compile
and evaluate expressions. An expression is a one-liner that returns a
value (mostly, but not limited to, Booleans).

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# looks like dev tool
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Resources/bin/generate_operator_regex.php .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/ExpressionLanguage
%{php_pear_dir}/Symfony/Component/ExpressionLanguage/*.php
%{php_pear_dir}/Symfony/Component/ExpressionLanguage/Node
%{php_pear_dir}/Symfony/Component/ExpressionLanguage/ParserCache
