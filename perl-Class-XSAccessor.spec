%define upstream_name Class-XSAccessor
%define upstream_version 1.14

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Class::XSAccessor::Heavy\\)'
%endif

%define debug_package %{nil}

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Generate fast XS accessors without runtime compilation
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(AutoXS::Header)
BuildRequires:	perl-devel

Provides:	perl-Class-XSAccessor-Array = %{version}-%{release}

%description
Class::XSAccessor implements fast read, write and read/write accessors in
XS. Additionally, it can provide predicates such as 'has_foo()' for testing
whether the attribute 'foo' is defined in the object. It only works with
objects that are implemented as ordinary hashes. the
Class::XSAccessor::Array manpage implements the same interface for objects
that use arrays for their internal representation.

Since version 0.10, the module can also generate simple constructors
(implemented in XS) for you. Simply supply the 'constructor =>
'constructor_name'' option or the 'constructors => ['new', 'create',
'spawn']' option. These constructors do the equivalent of the following
perl code:

  sub new {
    my $class = shift;
    return bless { @_ }, ref($class)||$class;
  }

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-5mdv2012.0
+ Revision: 765093
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-4
+ Revision: 763558
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.110.0-3
+ Revision: 676502
- rebuild
- rebuild

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.0-1mdv2011.0
+ Revision: 612058
- update to new version 1.11

* Thu Dec 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 604708
- update to new version 1.10

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-2mdv2011.0
+ Revision: 596744
- use meta.yml to fetch requires

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.90.0-1mdv2011.0
+ Revision: 595084
- update to new version 1.09

* Tue Aug 17 2010 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 570739
- update to 1.07

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-3mdv2011.0
+ Revision: 555219
- rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-2mdv2011.0
+ Revision: 552245
- obsoletes perl-class-xsaccesor-array, which has been merged in this dist

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.1
+ Revision: 466428
- update to 1.05

* Mon Jun 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 381799
- update to 1.03
- using %%perl_convert_version
- fixed license tag

* Mon May 18 2009 Jérôme Quelin <jquelin@mandriva.org> 1.02-1mdv2010.0
+ Revision: 377253
- update to new version 1.02
- update to 1.01

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.1
+ Revision: 314242
- update to new version 0.14

* Sun Dec 07 2008 Jérôme Quelin <jquelin@mandriva.org> 0.13-1mdv2009.1
+ Revision: 311556
- update to new version 0.13

* Tue Dec 02 2008 Jérôme Quelin <jquelin@mandriva.org> 0.11-1mdv2009.1
+ Revision: 309267
- import perl-Class-XSAccessor


* Tue Dec 02 2008 cpan2dist 0.11-1mdv
- initial mdv release, generated with cpan2dist

