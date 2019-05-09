#
# spec file for package tklib
#

Name:           tklib
Url:            http://core.tcl.tk/tklib/
BuildRequires:  tcl >= 8.3.1
BuildRequires:  sed
Version:        0.6_git20190502
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        The standard Tk library
License:        TCL
Group:          Development/Libraries/Tcl
BuildArch:      noarch
Requires:       /bin/sh
Requires:       tcl >= 8.3.1
Source0:        %name-%version.tar.gz

%description
Tklib, the Tk Standard Library is a collection of Tcl packages
that provide utility functions useful to a large collection of Tk
programmers.
The home web site for this code is http://core.tcl.tk/tklib/.
At this web site, you will find mailing lists, web forums, databases
for bug reports and feature requests, the CVS repository (browsable
on the web, or read-only accessible via CVS ), and more.

%prep
%setup -q
sed -i 's/2.0.1/2.1.0/g' modules/plotchart/plotchart.tcl
sed -i 's/\/bin\/env tclsh8.5/\/usr\/bin\/tclsh/g' examples/canvas/demo_editpoints.tcl
sed -i 's/\/bin\/env tclsh8.5/\/usr\/bin\/tclsh/g' examples/canvas/demo_editquadconvex.tcl
sed -i 's/\/bin\/env tclsh8.5/\/usr\/bin\/tclsh/g' examples/canvas/demo_editquad.tcl
sed -i 's/\/bin\/env tclsh8.5/\/usr\/bin\/tclsh/g' examples/canvas/demo_editpoly.tcl
sed -i 's/\/bin\/env tclsh8.5/\/usr\/bin\/tclsh/g' examples/canvas/demo_draghigh.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/'  examples/controlwidget/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/'  examples/plotchart/*.tcl
sed -i 's/\/usr\/bin\/env wish/\/usr\/bin\/wish/'    examples/mentry/*.tcl
sed -i 's/\/usr\/bin\/env wish/\/usr\/bin\/wish/'    examples/tablelist/*.tcl
sed -i 's/\/usr\/bin\/env wish/\/usr\/bin\/wish/'    examples/wcb/*.tcl

%build

%install
tclsh ./installer.tcl -no-examples -no-html \
 -app-path   %buildroot/%_bindir \
 -pkg-path   %buildroot/%_datadir/tcl/%name%version \
 -nroff-path %buildroot%_mandir/mann \
 -no-wait -no-gui

%files
%defattr(-,root,root)
%doc license.terms README ChangeLog
%doc support/releases/history/README-*
%_datadir/tcl
%_bindir/*
%doc examples
%doc %_mandir/mann/*

%changelog

