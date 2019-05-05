#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : step
Version  : 19.04.0
Release  : 5
URL      : https://download.kde.org/stable/applications/19.04.0/src/step-19.04.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.0/src/step-19.04.0.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.0/src/step-19.04.0.tar.xz.sig
Summary  : Interactive Physical Simulator
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: step-bin = %{version}-%{release}
Requires: step-data = %{version}-%{release}
Requires: step-license = %{version}-%{release}
Requires: step-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : eigen-dev
BuildRequires : gmp-dev
BuildRequires : gsl-dev
BuildRequires : khtml-dev
BuildRequires : kjs-dev
BuildRequires : kplotting-dev
BuildRequires : mpfr-dev
BuildRequires : pkgconfig(cln)
BuildRequires : pkgconfig(gsl)
BuildRequires : pkgconfig(libqalculate)
BuildRequires : python3
BuildRequires : qtbase-dev mesa-dev

%description
*************************************************
**    Step: Interactive Physical Simulator     **
**    StepCore: Physical Simulation Library    **
*************************************************

%package bin
Summary: bin components for the step package.
Group: Binaries
Requires: step-data = %{version}-%{release}
Requires: step-license = %{version}-%{release}

%description bin
bin components for the step package.


%package data
Summary: data components for the step package.
Group: Data

%description data
data components for the step package.


%package doc
Summary: doc components for the step package.
Group: Documentation

%description doc
doc components for the step package.


%package license
Summary: license components for the step package.
Group: Default

%description license
license components for the step package.


%package locales
Summary: locales components for the step package.
Group: Default

%description locales
locales components for the step package.


%prep
%setup -q -n step-19.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557049093
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557049093
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/step
cp COPYING %{buildroot}/usr/share/package-licenses/step/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/step/COPYING.DOC
cp cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/step/cmake_modules_COPYING-CMAKE-SCRIPTS
pushd clr-build
%make_install
popd
%find_lang step

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/step

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.step.desktop
/usr/share/config.kcfg/step.kcfg
/usr/share/icons/hicolor/128x128/apps/step.png
/usr/share/icons/hicolor/16x16/apps/step.png
/usr/share/icons/hicolor/22x22/actions/pointer.png
/usr/share/icons/hicolor/22x22/actions/step_object_Anchor.png
/usr/share/icons/hicolor/22x22/actions/step_object_Box.png
/usr/share/icons/hicolor/22x22/actions/step_object_ChargedParticle.png
/usr/share/icons/hicolor/22x22/actions/step_object_CircularMotor.png
/usr/share/icons/hicolor/22x22/actions/step_object_Controller.png
/usr/share/icons/hicolor/22x22/actions/step_object_CoulombForce.png
/usr/share/icons/hicolor/22x22/actions/step_object_Disk.png
/usr/share/icons/hicolor/22x22/actions/step_object_Gas.png
/usr/share/icons/hicolor/22x22/actions/step_object_GasParticle.png
/usr/share/icons/hicolor/22x22/actions/step_object_Graph.png
/usr/share/icons/hicolor/22x22/actions/step_object_GravitationForce.png
/usr/share/icons/hicolor/22x22/actions/step_object_LinearMotor.png
/usr/share/icons/hicolor/22x22/actions/step_object_Meter.png
/usr/share/icons/hicolor/22x22/actions/step_object_Note.png
/usr/share/icons/hicolor/22x22/actions/step_object_Particle.png
/usr/share/icons/hicolor/22x22/actions/step_object_Pin.png
/usr/share/icons/hicolor/22x22/actions/step_object_Polygon.png
/usr/share/icons/hicolor/22x22/actions/step_object_Rope.png
/usr/share/icons/hicolor/22x22/actions/step_object_SoftBody.png
/usr/share/icons/hicolor/22x22/actions/step_object_Spring.png
/usr/share/icons/hicolor/22x22/actions/step_object_Stick.png
/usr/share/icons/hicolor/22x22/actions/step_object_Tracer.png
/usr/share/icons/hicolor/22x22/actions/step_object_WeightForce.png
/usr/share/icons/hicolor/22x22/apps/step.png
/usr/share/icons/hicolor/32x32/apps/step.png
/usr/share/icons/hicolor/48x48/apps/step.png
/usr/share/icons/hicolor/64x64/apps/step.png
/usr/share/kxmlgui5/step/stepui.rc
/usr/share/locale/bg/LC_MESSAGES/step_qt.qm
/usr/share/locale/bs/LC_MESSAGES/step_qt.qm
/usr/share/locale/ca/LC_MESSAGES/step_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/step_qt.qm
/usr/share/locale/cs/LC_MESSAGES/step_qt.qm
/usr/share/locale/da/LC_MESSAGES/step_qt.qm
/usr/share/locale/de/LC_MESSAGES/step_qt.qm
/usr/share/locale/el/LC_MESSAGES/step_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/step_qt.qm
/usr/share/locale/eo/LC_MESSAGES/step_qt.qm
/usr/share/locale/es/LC_MESSAGES/step_qt.qm
/usr/share/locale/et/LC_MESSAGES/step_qt.qm
/usr/share/locale/fi/LC_MESSAGES/step_qt.qm
/usr/share/locale/fr/LC_MESSAGES/step_qt.qm
/usr/share/locale/ga/LC_MESSAGES/step_qt.qm
/usr/share/locale/gl/LC_MESSAGES/step_qt.qm
/usr/share/locale/hr/LC_MESSAGES/step_qt.qm
/usr/share/locale/hu/LC_MESSAGES/step_qt.qm
/usr/share/locale/it/LC_MESSAGES/step_qt.qm
/usr/share/locale/ja/LC_MESSAGES/step_qt.qm
/usr/share/locale/kk/LC_MESSAGES/step_qt.qm
/usr/share/locale/km/LC_MESSAGES/step_qt.qm
/usr/share/locale/lt/LC_MESSAGES/step_qt.qm
/usr/share/locale/lv/LC_MESSAGES/step_qt.qm
/usr/share/locale/mr/LC_MESSAGES/step_qt.qm
/usr/share/locale/nb/LC_MESSAGES/step_qt.qm
/usr/share/locale/nds/LC_MESSAGES/step_qt.qm
/usr/share/locale/nl/LC_MESSAGES/step_qt.qm
/usr/share/locale/nn/LC_MESSAGES/step_qt.qm
/usr/share/locale/nn/LC_SCRIPTS/step/step.js
/usr/share/locale/pa/LC_MESSAGES/step_qt.qm
/usr/share/locale/pl/LC_MESSAGES/step_qt.qm
/usr/share/locale/pt/LC_MESSAGES/step_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/step_qt.qm
/usr/share/locale/ro/LC_MESSAGES/step_qt.qm
/usr/share/locale/ru/LC_MESSAGES/step_qt.qm
/usr/share/locale/sk/LC_MESSAGES/step_qt.qm
/usr/share/locale/sl/LC_MESSAGES/step_qt.qm
/usr/share/locale/sv/LC_MESSAGES/step_qt.qm
/usr/share/locale/tr/LC_MESSAGES/step_qt.qm
/usr/share/locale/ug/LC_MESSAGES/step_qt.qm
/usr/share/locale/uk/LC_MESSAGES/step_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/step_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/step_qt.qm
/usr/share/metainfo/org.kde.step.appdata.xml
/usr/share/step/examples/brownian.step
/usr/share/step/examples/doublependulum.step
/usr/share/step/examples/eightpendula.step
/usr/share/step/examples/first.step
/usr/share/step/examples/fourpendula.step
/usr/share/step/examples/gas.step
/usr/share/step/examples/graph.step
/usr/share/step/examples/liquid.step
/usr/share/step/examples/lissajous.step
/usr/share/step/examples/motor.step
/usr/share/step/examples/motor1.step
/usr/share/step/examples/note.step
/usr/share/step/examples/resonance.step
/usr/share/step/examples/softbody.step
/usr/share/step/examples/solar.step
/usr/share/step/examples/springs.step
/usr/share/step/examples/wave.step
/usr/share/step/objinfo/Anchor.html
/usr/share/step/objinfo/Box.html
/usr/share/step/objinfo/ChargedParticle.html
/usr/share/step/objinfo/CoulombForce.html
/usr/share/step/objinfo/Disk.html
/usr/share/step/objinfo/Gas.html
/usr/share/step/objinfo/GasLJForce.html
/usr/share/step/objinfo/GasParticle.html
/usr/share/step/objinfo/GravitationForce.html
/usr/share/step/objinfo/LinearMotor.html
/usr/share/step/objinfo/Meter.html
/usr/share/step/objinfo/Note.html
/usr/share/step/objinfo/Particle.html
/usr/share/step/objinfo/Pin.html
/usr/share/step/objinfo/Polygon.html
/usr/share/step/objinfo/Spring.html
/usr/share/step/objinfo/WeightForce.html
/usr/share/step/objinfo/World.html
/usr/share/step/objinfo/l10n/de/Anchor.html
/usr/share/step/objinfo/l10n/de/Box.html
/usr/share/step/objinfo/l10n/de/ChargedParticle.html
/usr/share/step/objinfo/l10n/de/CoulombForce.html
/usr/share/step/objinfo/l10n/de/Disk.html
/usr/share/step/objinfo/l10n/de/Gas.html
/usr/share/step/objinfo/l10n/de/GasLJForce.html
/usr/share/step/objinfo/l10n/de/GasParticle.html
/usr/share/step/objinfo/l10n/de/GravitationForce.html
/usr/share/step/objinfo/l10n/de/LinearMotor.html
/usr/share/step/objinfo/l10n/de/Meter.html
/usr/share/step/objinfo/l10n/de/Note.html
/usr/share/step/objinfo/l10n/de/Particle.html
/usr/share/step/objinfo/l10n/de/Pin.html
/usr/share/step/objinfo/l10n/de/Polygon.html
/usr/share/step/objinfo/l10n/de/Spring.html
/usr/share/step/objinfo/l10n/de/WeightForce.html
/usr/share/step/objinfo/l10n/de/World.html
/usr/share/step/objinfo/l10n/it/Box.html
/usr/share/step/objinfo/l10n/it/ChargedParticle.html
/usr/share/step/objinfo/l10n/it/Disk.html
/usr/share/step/objinfo/l10n/it/Gas.html
/usr/share/step/objinfo/l10n/it/GasParticle.html
/usr/share/step/objinfo/l10n/it/Meter.html
/usr/share/step/objinfo/l10n/it/Note.html
/usr/share/step/objinfo/l10n/it/Particle.html
/usr/share/step/objinfo/l10n/it/Polygon.html
/usr/share/step/objinfo/l10n/it/Spring.html
/usr/share/step/objinfo/l10n/it/World.html
/usr/share/step/objinfo/l10n/ru/Anchor.html
/usr/share/step/objinfo/l10n/ru/Box.html
/usr/share/step/objinfo/l10n/ru/ChargedParticle.html
/usr/share/step/objinfo/l10n/ru/CoulombForce.html
/usr/share/step/objinfo/l10n/ru/Disk.html
/usr/share/step/objinfo/l10n/ru/Gas.html
/usr/share/step/objinfo/l10n/ru/GasLJForce.html
/usr/share/step/objinfo/l10n/ru/GasParticle.html
/usr/share/step/objinfo/l10n/ru/GravitationForce.html
/usr/share/step/objinfo/l10n/ru/LinearMotor.html
/usr/share/step/objinfo/l10n/ru/Meter.html
/usr/share/step/objinfo/l10n/ru/Note.html
/usr/share/step/objinfo/l10n/ru/Particle.html
/usr/share/step/objinfo/l10n/ru/Pin.html
/usr/share/step/objinfo/l10n/ru/Polygon.html
/usr/share/step/objinfo/l10n/ru/Spring.html
/usr/share/step/objinfo/l10n/ru/WeightForce.html
/usr/share/step/objinfo/l10n/ru/World.html
/usr/share/step/objinfo/l10n/uk/Anchor.html
/usr/share/step/objinfo/l10n/uk/Box.html
/usr/share/step/objinfo/l10n/uk/ChargedParticle.html
/usr/share/step/objinfo/l10n/uk/CoulombForce.html
/usr/share/step/objinfo/l10n/uk/Disk.html
/usr/share/step/objinfo/l10n/uk/Gas.html
/usr/share/step/objinfo/l10n/uk/GasLJForce.html
/usr/share/step/objinfo/l10n/uk/GasParticle.html
/usr/share/step/objinfo/l10n/uk/GravitationForce.html
/usr/share/step/objinfo/l10n/uk/LinearMotor.html
/usr/share/step/objinfo/l10n/uk/Meter.html
/usr/share/step/objinfo/l10n/uk/Note.html
/usr/share/step/objinfo/l10n/uk/Particle.html
/usr/share/step/objinfo/l10n/uk/Pin.html
/usr/share/step/objinfo/l10n/uk/Polygon.html
/usr/share/step/objinfo/l10n/uk/Spring.html
/usr/share/step/objinfo/l10n/uk/WeightForce.html
/usr/share/step/objinfo/l10n/uk/World.html
/usr/share/step/tutorials/tutorial1.step
/usr/share/step/tutorials/tutorial2.step
/usr/share/step/tutorials/tutorial3.step
/usr/share/step/tutorials/tutorial4.step
/usr/share/step/tutorials/tutorial5.step
/usr/share/xdg/step.knsrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/step/examples.docbook
/usr/share/doc/HTML/ca/step/index.cache.bz2
/usr/share/doc/HTML/ca/step/index.docbook
/usr/share/doc/HTML/ca/step/tutorials.docbook
/usr/share/doc/HTML/de/step/examples.docbook
/usr/share/doc/HTML/de/step/index.cache.bz2
/usr/share/doc/HTML/de/step/index.docbook
/usr/share/doc/HTML/de/step/mainwindow.png
/usr/share/doc/HTML/de/step/tutorials.docbook
/usr/share/doc/HTML/en/step/circular-motor.png
/usr/share/doc/HTML/en/step/disk-properties.png
/usr/share/doc/HTML/en/step/examples.docbook
/usr/share/doc/HTML/en/step/index.cache.bz2
/usr/share/doc/HTML/en/step/index.docbook
/usr/share/doc/HTML/en/step/mainwindow.png
/usr/share/doc/HTML/en/step/tutorial1.png
/usr/share/doc/HTML/en/step/tutorial2.png
/usr/share/doc/HTML/en/step/tutorial3.png
/usr/share/doc/HTML/en/step/tutorial4.png
/usr/share/doc/HTML/en/step/tutorial5.png
/usr/share/doc/HTML/en/step/tutorials.docbook
/usr/share/doc/HTML/es/step/examples.docbook
/usr/share/doc/HTML/es/step/index.cache.bz2
/usr/share/doc/HTML/es/step/index.docbook
/usr/share/doc/HTML/es/step/tutorials.docbook
/usr/share/doc/HTML/et/step/examples.docbook
/usr/share/doc/HTML/et/step/index.cache.bz2
/usr/share/doc/HTML/et/step/index.docbook
/usr/share/doc/HTML/et/step/tutorials.docbook
/usr/share/doc/HTML/it/step/examples.docbook
/usr/share/doc/HTML/it/step/index.cache.bz2
/usr/share/doc/HTML/it/step/index.docbook
/usr/share/doc/HTML/it/step/tutorials.docbook
/usr/share/doc/HTML/nl/step/examples.docbook
/usr/share/doc/HTML/nl/step/index.cache.bz2
/usr/share/doc/HTML/nl/step/index.docbook
/usr/share/doc/HTML/nl/step/tutorials.docbook
/usr/share/doc/HTML/pt_BR/step/examples.docbook
/usr/share/doc/HTML/pt_BR/step/index.cache.bz2
/usr/share/doc/HTML/pt_BR/step/index.docbook
/usr/share/doc/HTML/pt_BR/step/tutorials.docbook
/usr/share/doc/HTML/sv/step/examples.docbook
/usr/share/doc/HTML/sv/step/index.cache.bz2
/usr/share/doc/HTML/sv/step/index.docbook
/usr/share/doc/HTML/sv/step/tutorials.docbook
/usr/share/doc/HTML/uk/step/examples.docbook
/usr/share/doc/HTML/uk/step/index.cache.bz2
/usr/share/doc/HTML/uk/step/index.docbook
/usr/share/doc/HTML/uk/step/mainwindow.png
/usr/share/doc/HTML/uk/step/tutorials.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/step/COPYING
/usr/share/package-licenses/step/COPYING.DOC
/usr/share/package-licenses/step/cmake_modules_COPYING-CMAKE-SCRIPTS

%files locales -f step.lang
%defattr(-,root,root,-)

