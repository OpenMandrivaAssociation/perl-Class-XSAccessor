%define debug_package %{nil}

%define upstream_name Class-XSAccessor
%define upstream_version 1.19

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Class::XSAccessor::Heavy\\)'
%endif

Summary:	Generate fast XS accessors without runtime compilation
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/Class-XSAccessor-%{upstream_version}.tar.gz
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
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{perl_vendorlib}/*
%{_mandir}/man3/*



