%define		pearname	ExpressionLanguage
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 ExpressionLanguage Component
Name:		php-symfony2-ExpressionLanguage
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/expression-language/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	168a499dccfe05892b4cd72e126a1741
URL:		http://symfony.com/doc/2.4/components/expression_language/index.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-pear
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
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests
# dev
rm $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Resources/bin/generate_operator_regex.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/ExpressionLanguage
%{php_pear_dir}/Symfony/Component/ExpressionLanguage/*.php
%{php_pear_dir}/Symfony/Component/ExpressionLanguage/Node
%{php_pear_dir}/Symfony/Component/ExpressionLanguage/ParserCache
