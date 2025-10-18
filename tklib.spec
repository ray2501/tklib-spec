#
# spec file for package tklib
#

Name:           tklib
Url:            http://core.tcl.tk/tklib/
BuildRequires:  tcl >= 8.6.1
BuildRequires:  sed
Version:        0.9_git20251017
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        The standard Tk library
License:        TCL
Group:          Development/Libraries/Tcl
BuildArch:      noarch
Requires:       /bin/sh
Requires:       tcl >= 8.6.1
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
%setup -q -n %{name}-%{version}
sed -i 's/2.0.1/2.1.0/g' modules/plotchart/plotchart.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  apps/bitmap-editor
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  apps/diagram-viewer
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  apps/shtmlview
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/canvas/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/controlwidget/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/map/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/mentry/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/menubar/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/ntext/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/persistentSelection/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/plotchart/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/scrollutil/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/tablelist/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/tkpiechart/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/tsw/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/widget/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/widgetPlus/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  examples/wcb/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  modules/ctext/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  modules/text/txmixins.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/g'  modules/treeview/tvmixins.tcl


chmod -x examples/diagrams/*.tcl
chmod -x examples/plotchart/tcllogo.gif
chmod -x modules/*/*.tcl

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

