
%define realname   Class-XSAccessor
%define version    1.01
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Generate fast XS accessors without runtime compilation
Source:     http://www.cpan.org/modules/by-module/Class/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(AutoXS::Header)



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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


