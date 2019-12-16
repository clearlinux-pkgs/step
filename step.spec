#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : step
Version  : 19.12.0
Release  : 15
URL      : https://download.kde.org/stable/release-service/19.12.0/src/step-19.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.0/src/step-19.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.0/src/step-19.12.0.tar.xz.sig
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
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : gmp-dev
BuildRequires : gsl-dev
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
%setup -q -n step-19.12.0
cd %{_builddir}/step-19.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576536369
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1576536369
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/step
cp %{_builddir}/step-19.12.0/COPYING %{buildroot}/usr/share/package-licenses/step/40f6a79e31db3f532867ecebb7186eef8a34ff76
cp %{_builddir}/step-19.12.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/step/0c4be15f5177aafffe980ca09c0f4ca6ed741f43
cp %{_builddir}/step-19.12.0/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/step/ff3ed70db4739b3c6747c7f624fe2bad70802987
pushd clr-build
%make_install
popd
%find_lang step
%find_lang step_example_files
%find_lang step_objinfo_files

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
/usr/share/locale/ml/LC_MESSAGES/step_qt.qm
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
/usr/share/mime-packages/org.kde.step.xml
/usr/share/step/examples/brownian.step
/usr/share/step/examples/ca/brownian.step
/usr/share/step/examples/ca/doublependulum.step
/usr/share/step/examples/ca/eightpendula.step
/usr/share/step/examples/ca/first.step
/usr/share/step/examples/ca/fourpendula.step
/usr/share/step/examples/ca/gas.step
/usr/share/step/examples/ca/graph.step
/usr/share/step/examples/ca/liquid.step
/usr/share/step/examples/ca/lissajous.step
/usr/share/step/examples/ca/motor.step
/usr/share/step/examples/ca/motor1.step
/usr/share/step/examples/ca/note.step
/usr/share/step/examples/ca/resonance.step
/usr/share/step/examples/ca/softbody.step
/usr/share/step/examples/ca/solar.step
/usr/share/step/examples/ca/springs.step
/usr/share/step/examples/ca/wave.step
/usr/share/step/examples/doublependulum.step
/usr/share/step/examples/eightpendula.step
/usr/share/step/examples/en_GB/brownian.step
/usr/share/step/examples/en_GB/doublependulum.step
/usr/share/step/examples/en_GB/eightpendula.step
/usr/share/step/examples/en_GB/first.step
/usr/share/step/examples/en_GB/fourpendula.step
/usr/share/step/examples/en_GB/gas.step
/usr/share/step/examples/en_GB/graph.step
/usr/share/step/examples/en_GB/liquid.step
/usr/share/step/examples/en_GB/lissajous.step
/usr/share/step/examples/en_GB/motor.step
/usr/share/step/examples/en_GB/motor1.step
/usr/share/step/examples/en_GB/note.step
/usr/share/step/examples/en_GB/resonance.step
/usr/share/step/examples/en_GB/softbody.step
/usr/share/step/examples/en_GB/solar.step
/usr/share/step/examples/en_GB/springs.step
/usr/share/step/examples/en_GB/wave.step
/usr/share/step/examples/es/brownian.step
/usr/share/step/examples/es/doublependulum.step
/usr/share/step/examples/es/eightpendula.step
/usr/share/step/examples/es/first.step
/usr/share/step/examples/es/fourpendula.step
/usr/share/step/examples/es/gas.step
/usr/share/step/examples/es/graph.step
/usr/share/step/examples/es/liquid.step
/usr/share/step/examples/es/lissajous.step
/usr/share/step/examples/es/motor.step
/usr/share/step/examples/es/motor1.step
/usr/share/step/examples/es/note.step
/usr/share/step/examples/es/resonance.step
/usr/share/step/examples/es/softbody.step
/usr/share/step/examples/es/solar.step
/usr/share/step/examples/es/springs.step
/usr/share/step/examples/es/wave.step
/usr/share/step/examples/first.step
/usr/share/step/examples/fourpendula.step
/usr/share/step/examples/fr/brownian.step
/usr/share/step/examples/fr/doublependulum.step
/usr/share/step/examples/fr/eightpendula.step
/usr/share/step/examples/fr/first.step
/usr/share/step/examples/fr/fourpendula.step
/usr/share/step/examples/fr/gas.step
/usr/share/step/examples/fr/graph.step
/usr/share/step/examples/fr/liquid.step
/usr/share/step/examples/fr/lissajous.step
/usr/share/step/examples/fr/motor.step
/usr/share/step/examples/fr/motor1.step
/usr/share/step/examples/fr/note.step
/usr/share/step/examples/fr/resonance.step
/usr/share/step/examples/fr/softbody.step
/usr/share/step/examples/fr/solar.step
/usr/share/step/examples/fr/springs.step
/usr/share/step/examples/fr/wave.step
/usr/share/step/examples/gas.step
/usr/share/step/examples/graph.step
/usr/share/step/examples/liquid.step
/usr/share/step/examples/lissajous.step
/usr/share/step/examples/motor.step
/usr/share/step/examples/motor1.step
/usr/share/step/examples/nl/brownian.step
/usr/share/step/examples/nl/doublependulum.step
/usr/share/step/examples/nl/eightpendula.step
/usr/share/step/examples/nl/first.step
/usr/share/step/examples/nl/fourpendula.step
/usr/share/step/examples/nl/gas.step
/usr/share/step/examples/nl/graph.step
/usr/share/step/examples/nl/liquid.step
/usr/share/step/examples/nl/lissajous.step
/usr/share/step/examples/nl/motor.step
/usr/share/step/examples/nl/motor1.step
/usr/share/step/examples/nl/note.step
/usr/share/step/examples/nl/resonance.step
/usr/share/step/examples/nl/softbody.step
/usr/share/step/examples/nl/solar.step
/usr/share/step/examples/nl/springs.step
/usr/share/step/examples/nl/wave.step
/usr/share/step/examples/note.step
/usr/share/step/examples/pt/brownian.step
/usr/share/step/examples/pt/doublependulum.step
/usr/share/step/examples/pt/eightpendula.step
/usr/share/step/examples/pt/first.step
/usr/share/step/examples/pt/fourpendula.step
/usr/share/step/examples/pt/gas.step
/usr/share/step/examples/pt/graph.step
/usr/share/step/examples/pt/liquid.step
/usr/share/step/examples/pt/lissajous.step
/usr/share/step/examples/pt/motor.step
/usr/share/step/examples/pt/motor1.step
/usr/share/step/examples/pt/note.step
/usr/share/step/examples/pt/resonance.step
/usr/share/step/examples/pt/softbody.step
/usr/share/step/examples/pt/solar.step
/usr/share/step/examples/pt/springs.step
/usr/share/step/examples/pt/wave.step
/usr/share/step/examples/pt_BR/brownian.step
/usr/share/step/examples/pt_BR/doublependulum.step
/usr/share/step/examples/pt_BR/eightpendula.step
/usr/share/step/examples/pt_BR/first.step
/usr/share/step/examples/pt_BR/fourpendula.step
/usr/share/step/examples/pt_BR/gas.step
/usr/share/step/examples/pt_BR/graph.step
/usr/share/step/examples/pt_BR/liquid.step
/usr/share/step/examples/pt_BR/lissajous.step
/usr/share/step/examples/pt_BR/motor.step
/usr/share/step/examples/pt_BR/motor1.step
/usr/share/step/examples/pt_BR/note.step
/usr/share/step/examples/pt_BR/resonance.step
/usr/share/step/examples/pt_BR/softbody.step
/usr/share/step/examples/pt_BR/solar.step
/usr/share/step/examples/pt_BR/springs.step
/usr/share/step/examples/pt_BR/wave.step
/usr/share/step/examples/resonance.step
/usr/share/step/examples/ru/brownian.step
/usr/share/step/examples/ru/doublependulum.step
/usr/share/step/examples/ru/eightpendula.step
/usr/share/step/examples/ru/first.step
/usr/share/step/examples/ru/fourpendula.step
/usr/share/step/examples/ru/gas.step
/usr/share/step/examples/ru/graph.step
/usr/share/step/examples/ru/liquid.step
/usr/share/step/examples/ru/lissajous.step
/usr/share/step/examples/ru/motor.step
/usr/share/step/examples/ru/motor1.step
/usr/share/step/examples/ru/note.step
/usr/share/step/examples/ru/resonance.step
/usr/share/step/examples/ru/softbody.step
/usr/share/step/examples/ru/solar.step
/usr/share/step/examples/ru/springs.step
/usr/share/step/examples/ru/wave.step
/usr/share/step/examples/sk/brownian.step
/usr/share/step/examples/sk/doublependulum.step
/usr/share/step/examples/sk/eightpendula.step
/usr/share/step/examples/sk/first.step
/usr/share/step/examples/sk/fourpendula.step
/usr/share/step/examples/sk/gas.step
/usr/share/step/examples/sk/graph.step
/usr/share/step/examples/sk/liquid.step
/usr/share/step/examples/sk/lissajous.step
/usr/share/step/examples/sk/motor.step
/usr/share/step/examples/sk/motor1.step
/usr/share/step/examples/sk/note.step
/usr/share/step/examples/sk/resonance.step
/usr/share/step/examples/sk/softbody.step
/usr/share/step/examples/sk/solar.step
/usr/share/step/examples/sk/springs.step
/usr/share/step/examples/sk/wave.step
/usr/share/step/examples/softbody.step
/usr/share/step/examples/solar.step
/usr/share/step/examples/springs.step
/usr/share/step/examples/uk/brownian.step
/usr/share/step/examples/uk/doublependulum.step
/usr/share/step/examples/uk/eightpendula.step
/usr/share/step/examples/uk/first.step
/usr/share/step/examples/uk/fourpendula.step
/usr/share/step/examples/uk/gas.step
/usr/share/step/examples/uk/graph.step
/usr/share/step/examples/uk/liquid.step
/usr/share/step/examples/uk/lissajous.step
/usr/share/step/examples/uk/motor.step
/usr/share/step/examples/uk/motor1.step
/usr/share/step/examples/uk/note.step
/usr/share/step/examples/uk/resonance.step
/usr/share/step/examples/uk/softbody.step
/usr/share/step/examples/uk/solar.step
/usr/share/step/examples/uk/springs.step
/usr/share/step/examples/uk/wave.step
/usr/share/step/examples/wave.step
/usr/share/step/examples/zh_TW/brownian.step
/usr/share/step/examples/zh_TW/doublependulum.step
/usr/share/step/examples/zh_TW/eightpendula.step
/usr/share/step/examples/zh_TW/first.step
/usr/share/step/examples/zh_TW/fourpendula.step
/usr/share/step/examples/zh_TW/gas.step
/usr/share/step/examples/zh_TW/graph.step
/usr/share/step/examples/zh_TW/liquid.step
/usr/share/step/examples/zh_TW/lissajous.step
/usr/share/step/examples/zh_TW/motor.step
/usr/share/step/examples/zh_TW/motor1.step
/usr/share/step/examples/zh_TW/note.step
/usr/share/step/examples/zh_TW/resonance.step
/usr/share/step/examples/zh_TW/softbody.step
/usr/share/step/examples/zh_TW/solar.step
/usr/share/step/examples/zh_TW/springs.step
/usr/share/step/examples/zh_TW/wave.step
/usr/share/step/objinfo/anchor.html
/usr/share/step/objinfo/box.html
/usr/share/step/objinfo/chargedparticle.html
/usr/share/step/objinfo/coulombforce.html
/usr/share/step/objinfo/disk.html
/usr/share/step/objinfo/gas.html
/usr/share/step/objinfo/gasljforce.html
/usr/share/step/objinfo/gasparticle.html
/usr/share/step/objinfo/gravitationforce.html
/usr/share/step/objinfo/l10n/ca/anchor.html
/usr/share/step/objinfo/l10n/ca/box.html
/usr/share/step/objinfo/l10n/ca/chargedparticle.html
/usr/share/step/objinfo/l10n/ca/coulombforce.html
/usr/share/step/objinfo/l10n/ca/disk.html
/usr/share/step/objinfo/l10n/ca/gas.html
/usr/share/step/objinfo/l10n/ca/gasljforce.html
/usr/share/step/objinfo/l10n/ca/gasparticle.html
/usr/share/step/objinfo/l10n/ca/gravitationforce.html
/usr/share/step/objinfo/l10n/ca/linearmotor.html
/usr/share/step/objinfo/l10n/ca/meter.html
/usr/share/step/objinfo/l10n/ca/note.html
/usr/share/step/objinfo/l10n/ca/particle.html
/usr/share/step/objinfo/l10n/ca/pin.html
/usr/share/step/objinfo/l10n/ca/polygon.html
/usr/share/step/objinfo/l10n/ca/softbody.html
/usr/share/step/objinfo/l10n/ca/spring.html
/usr/share/step/objinfo/l10n/ca/weightforce.html
/usr/share/step/objinfo/l10n/ca/world.html
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
/usr/share/step/objinfo/l10n/en_GB/anchor.html
/usr/share/step/objinfo/l10n/en_GB/box.html
/usr/share/step/objinfo/l10n/en_GB/chargedparticle.html
/usr/share/step/objinfo/l10n/en_GB/coulombforce.html
/usr/share/step/objinfo/l10n/en_GB/disk.html
/usr/share/step/objinfo/l10n/en_GB/gas.html
/usr/share/step/objinfo/l10n/en_GB/gasljforce.html
/usr/share/step/objinfo/l10n/en_GB/gasparticle.html
/usr/share/step/objinfo/l10n/en_GB/gravitationforce.html
/usr/share/step/objinfo/l10n/en_GB/linearmotor.html
/usr/share/step/objinfo/l10n/en_GB/meter.html
/usr/share/step/objinfo/l10n/en_GB/note.html
/usr/share/step/objinfo/l10n/en_GB/particle.html
/usr/share/step/objinfo/l10n/en_GB/pin.html
/usr/share/step/objinfo/l10n/en_GB/polygon.html
/usr/share/step/objinfo/l10n/en_GB/softbody.html
/usr/share/step/objinfo/l10n/en_GB/spring.html
/usr/share/step/objinfo/l10n/en_GB/weightforce.html
/usr/share/step/objinfo/l10n/en_GB/world.html
/usr/share/step/objinfo/l10n/es/anchor.html
/usr/share/step/objinfo/l10n/es/box.html
/usr/share/step/objinfo/l10n/es/chargedparticle.html
/usr/share/step/objinfo/l10n/es/coulombforce.html
/usr/share/step/objinfo/l10n/es/disk.html
/usr/share/step/objinfo/l10n/es/gas.html
/usr/share/step/objinfo/l10n/es/gasljforce.html
/usr/share/step/objinfo/l10n/es/gasparticle.html
/usr/share/step/objinfo/l10n/es/gravitationforce.html
/usr/share/step/objinfo/l10n/es/linearmotor.html
/usr/share/step/objinfo/l10n/es/meter.html
/usr/share/step/objinfo/l10n/es/note.html
/usr/share/step/objinfo/l10n/es/particle.html
/usr/share/step/objinfo/l10n/es/pin.html
/usr/share/step/objinfo/l10n/es/polygon.html
/usr/share/step/objinfo/l10n/es/softbody.html
/usr/share/step/objinfo/l10n/es/spring.html
/usr/share/step/objinfo/l10n/es/weightforce.html
/usr/share/step/objinfo/l10n/es/world.html
/usr/share/step/objinfo/l10n/fr/anchor.html
/usr/share/step/objinfo/l10n/fr/box.html
/usr/share/step/objinfo/l10n/fr/chargedparticle.html
/usr/share/step/objinfo/l10n/fr/coulombforce.html
/usr/share/step/objinfo/l10n/fr/disk.html
/usr/share/step/objinfo/l10n/fr/gas.html
/usr/share/step/objinfo/l10n/fr/gasljforce.html
/usr/share/step/objinfo/l10n/fr/gasparticle.html
/usr/share/step/objinfo/l10n/fr/gravitationforce.html
/usr/share/step/objinfo/l10n/fr/linearmotor.html
/usr/share/step/objinfo/l10n/fr/meter.html
/usr/share/step/objinfo/l10n/fr/note.html
/usr/share/step/objinfo/l10n/fr/particle.html
/usr/share/step/objinfo/l10n/fr/pin.html
/usr/share/step/objinfo/l10n/fr/polygon.html
/usr/share/step/objinfo/l10n/fr/softbody.html
/usr/share/step/objinfo/l10n/fr/spring.html
/usr/share/step/objinfo/l10n/fr/weightforce.html
/usr/share/step/objinfo/l10n/fr/world.html
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
/usr/share/step/objinfo/l10n/it/anchor.html
/usr/share/step/objinfo/l10n/it/box.html
/usr/share/step/objinfo/l10n/it/chargedparticle.html
/usr/share/step/objinfo/l10n/it/coulombforce.html
/usr/share/step/objinfo/l10n/it/disk.html
/usr/share/step/objinfo/l10n/it/gas.html
/usr/share/step/objinfo/l10n/it/gasljforce.html
/usr/share/step/objinfo/l10n/it/gasparticle.html
/usr/share/step/objinfo/l10n/it/gravitationforce.html
/usr/share/step/objinfo/l10n/it/linearmotor.html
/usr/share/step/objinfo/l10n/it/meter.html
/usr/share/step/objinfo/l10n/it/note.html
/usr/share/step/objinfo/l10n/it/particle.html
/usr/share/step/objinfo/l10n/it/pin.html
/usr/share/step/objinfo/l10n/it/polygon.html
/usr/share/step/objinfo/l10n/it/softbody.html
/usr/share/step/objinfo/l10n/it/spring.html
/usr/share/step/objinfo/l10n/it/weightforce.html
/usr/share/step/objinfo/l10n/it/world.html
/usr/share/step/objinfo/l10n/nl/anchor.html
/usr/share/step/objinfo/l10n/nl/box.html
/usr/share/step/objinfo/l10n/nl/chargedparticle.html
/usr/share/step/objinfo/l10n/nl/coulombforce.html
/usr/share/step/objinfo/l10n/nl/disk.html
/usr/share/step/objinfo/l10n/nl/gas.html
/usr/share/step/objinfo/l10n/nl/gasljforce.html
/usr/share/step/objinfo/l10n/nl/gasparticle.html
/usr/share/step/objinfo/l10n/nl/gravitationforce.html
/usr/share/step/objinfo/l10n/nl/linearmotor.html
/usr/share/step/objinfo/l10n/nl/meter.html
/usr/share/step/objinfo/l10n/nl/note.html
/usr/share/step/objinfo/l10n/nl/particle.html
/usr/share/step/objinfo/l10n/nl/pin.html
/usr/share/step/objinfo/l10n/nl/polygon.html
/usr/share/step/objinfo/l10n/nl/softbody.html
/usr/share/step/objinfo/l10n/nl/spring.html
/usr/share/step/objinfo/l10n/nl/weightforce.html
/usr/share/step/objinfo/l10n/nl/world.html
/usr/share/step/objinfo/l10n/pt/anchor.html
/usr/share/step/objinfo/l10n/pt/box.html
/usr/share/step/objinfo/l10n/pt/chargedparticle.html
/usr/share/step/objinfo/l10n/pt/coulombforce.html
/usr/share/step/objinfo/l10n/pt/disk.html
/usr/share/step/objinfo/l10n/pt/gas.html
/usr/share/step/objinfo/l10n/pt/gasljforce.html
/usr/share/step/objinfo/l10n/pt/gasparticle.html
/usr/share/step/objinfo/l10n/pt/gravitationforce.html
/usr/share/step/objinfo/l10n/pt/linearmotor.html
/usr/share/step/objinfo/l10n/pt/meter.html
/usr/share/step/objinfo/l10n/pt/note.html
/usr/share/step/objinfo/l10n/pt/particle.html
/usr/share/step/objinfo/l10n/pt/pin.html
/usr/share/step/objinfo/l10n/pt/polygon.html
/usr/share/step/objinfo/l10n/pt/softbody.html
/usr/share/step/objinfo/l10n/pt/spring.html
/usr/share/step/objinfo/l10n/pt/weightforce.html
/usr/share/step/objinfo/l10n/pt/world.html
/usr/share/step/objinfo/l10n/pt_BR/anchor.html
/usr/share/step/objinfo/l10n/pt_BR/box.html
/usr/share/step/objinfo/l10n/pt_BR/chargedparticle.html
/usr/share/step/objinfo/l10n/pt_BR/coulombforce.html
/usr/share/step/objinfo/l10n/pt_BR/disk.html
/usr/share/step/objinfo/l10n/pt_BR/gas.html
/usr/share/step/objinfo/l10n/pt_BR/gasljforce.html
/usr/share/step/objinfo/l10n/pt_BR/gasparticle.html
/usr/share/step/objinfo/l10n/pt_BR/gravitationforce.html
/usr/share/step/objinfo/l10n/pt_BR/linearmotor.html
/usr/share/step/objinfo/l10n/pt_BR/meter.html
/usr/share/step/objinfo/l10n/pt_BR/note.html
/usr/share/step/objinfo/l10n/pt_BR/particle.html
/usr/share/step/objinfo/l10n/pt_BR/pin.html
/usr/share/step/objinfo/l10n/pt_BR/polygon.html
/usr/share/step/objinfo/l10n/pt_BR/softbody.html
/usr/share/step/objinfo/l10n/pt_BR/spring.html
/usr/share/step/objinfo/l10n/pt_BR/weightforce.html
/usr/share/step/objinfo/l10n/pt_BR/world.html
/usr/share/step/objinfo/l10n/ru/anchor.html
/usr/share/step/objinfo/l10n/ru/box.html
/usr/share/step/objinfo/l10n/ru/chargedparticle.html
/usr/share/step/objinfo/l10n/ru/coulombforce.html
/usr/share/step/objinfo/l10n/ru/disk.html
/usr/share/step/objinfo/l10n/ru/gas.html
/usr/share/step/objinfo/l10n/ru/gasljforce.html
/usr/share/step/objinfo/l10n/ru/gasparticle.html
/usr/share/step/objinfo/l10n/ru/gravitationforce.html
/usr/share/step/objinfo/l10n/ru/linearmotor.html
/usr/share/step/objinfo/l10n/ru/meter.html
/usr/share/step/objinfo/l10n/ru/note.html
/usr/share/step/objinfo/l10n/ru/particle.html
/usr/share/step/objinfo/l10n/ru/pin.html
/usr/share/step/objinfo/l10n/ru/polygon.html
/usr/share/step/objinfo/l10n/ru/softbody.html
/usr/share/step/objinfo/l10n/ru/spring.html
/usr/share/step/objinfo/l10n/ru/weightforce.html
/usr/share/step/objinfo/l10n/ru/world.html
/usr/share/step/objinfo/l10n/sk/anchor.html
/usr/share/step/objinfo/l10n/sk/box.html
/usr/share/step/objinfo/l10n/sk/chargedparticle.html
/usr/share/step/objinfo/l10n/sk/coulombforce.html
/usr/share/step/objinfo/l10n/sk/disk.html
/usr/share/step/objinfo/l10n/sk/gas.html
/usr/share/step/objinfo/l10n/sk/gasljforce.html
/usr/share/step/objinfo/l10n/sk/gasparticle.html
/usr/share/step/objinfo/l10n/sk/gravitationforce.html
/usr/share/step/objinfo/l10n/sk/linearmotor.html
/usr/share/step/objinfo/l10n/sk/meter.html
/usr/share/step/objinfo/l10n/sk/note.html
/usr/share/step/objinfo/l10n/sk/particle.html
/usr/share/step/objinfo/l10n/sk/pin.html
/usr/share/step/objinfo/l10n/sk/polygon.html
/usr/share/step/objinfo/l10n/sk/softbody.html
/usr/share/step/objinfo/l10n/sk/spring.html
/usr/share/step/objinfo/l10n/sk/weightforce.html
/usr/share/step/objinfo/l10n/sk/world.html
/usr/share/step/objinfo/l10n/uk/anchor.html
/usr/share/step/objinfo/l10n/uk/box.html
/usr/share/step/objinfo/l10n/uk/chargedparticle.html
/usr/share/step/objinfo/l10n/uk/coulombforce.html
/usr/share/step/objinfo/l10n/uk/disk.html
/usr/share/step/objinfo/l10n/uk/gas.html
/usr/share/step/objinfo/l10n/uk/gasljforce.html
/usr/share/step/objinfo/l10n/uk/gasparticle.html
/usr/share/step/objinfo/l10n/uk/gravitationforce.html
/usr/share/step/objinfo/l10n/uk/linearmotor.html
/usr/share/step/objinfo/l10n/uk/meter.html
/usr/share/step/objinfo/l10n/uk/note.html
/usr/share/step/objinfo/l10n/uk/particle.html
/usr/share/step/objinfo/l10n/uk/pin.html
/usr/share/step/objinfo/l10n/uk/polygon.html
/usr/share/step/objinfo/l10n/uk/softbody.html
/usr/share/step/objinfo/l10n/uk/spring.html
/usr/share/step/objinfo/l10n/uk/weightforce.html
/usr/share/step/objinfo/l10n/uk/world.html
/usr/share/step/objinfo/l10n/zh_TW/anchor.html
/usr/share/step/objinfo/l10n/zh_TW/box.html
/usr/share/step/objinfo/l10n/zh_TW/chargedparticle.html
/usr/share/step/objinfo/l10n/zh_TW/coulombforce.html
/usr/share/step/objinfo/l10n/zh_TW/disk.html
/usr/share/step/objinfo/l10n/zh_TW/gas.html
/usr/share/step/objinfo/l10n/zh_TW/gasljforce.html
/usr/share/step/objinfo/l10n/zh_TW/gasparticle.html
/usr/share/step/objinfo/l10n/zh_TW/gravitationforce.html
/usr/share/step/objinfo/l10n/zh_TW/linearmotor.html
/usr/share/step/objinfo/l10n/zh_TW/meter.html
/usr/share/step/objinfo/l10n/zh_TW/note.html
/usr/share/step/objinfo/l10n/zh_TW/particle.html
/usr/share/step/objinfo/l10n/zh_TW/pin.html
/usr/share/step/objinfo/l10n/zh_TW/polygon.html
/usr/share/step/objinfo/l10n/zh_TW/softbody.html
/usr/share/step/objinfo/l10n/zh_TW/spring.html
/usr/share/step/objinfo/l10n/zh_TW/weightforce.html
/usr/share/step/objinfo/l10n/zh_TW/world.html
/usr/share/step/objinfo/linearmotor.html
/usr/share/step/objinfo/meter.html
/usr/share/step/objinfo/note.html
/usr/share/step/objinfo/particle.html
/usr/share/step/objinfo/pin.html
/usr/share/step/objinfo/polygon.html
/usr/share/step/objinfo/softbody.html
/usr/share/step/objinfo/spring.html
/usr/share/step/objinfo/weightforce.html
/usr/share/step/objinfo/world.html
/usr/share/step/tutorials/ca/tutorial1.step
/usr/share/step/tutorials/ca/tutorial2.step
/usr/share/step/tutorials/ca/tutorial3.step
/usr/share/step/tutorials/ca/tutorial4.step
/usr/share/step/tutorials/ca/tutorial5.step
/usr/share/step/tutorials/en_GB/tutorial1.step
/usr/share/step/tutorials/en_GB/tutorial2.step
/usr/share/step/tutorials/en_GB/tutorial3.step
/usr/share/step/tutorials/en_GB/tutorial4.step
/usr/share/step/tutorials/en_GB/tutorial5.step
/usr/share/step/tutorials/es/tutorial1.step
/usr/share/step/tutorials/es/tutorial2.step
/usr/share/step/tutorials/es/tutorial3.step
/usr/share/step/tutorials/es/tutorial4.step
/usr/share/step/tutorials/es/tutorial5.step
/usr/share/step/tutorials/fr/tutorial1.step
/usr/share/step/tutorials/fr/tutorial2.step
/usr/share/step/tutorials/fr/tutorial3.step
/usr/share/step/tutorials/fr/tutorial4.step
/usr/share/step/tutorials/fr/tutorial5.step
/usr/share/step/tutorials/nl/tutorial1.step
/usr/share/step/tutorials/nl/tutorial2.step
/usr/share/step/tutorials/nl/tutorial3.step
/usr/share/step/tutorials/nl/tutorial4.step
/usr/share/step/tutorials/nl/tutorial5.step
/usr/share/step/tutorials/pt/tutorial1.step
/usr/share/step/tutorials/pt/tutorial2.step
/usr/share/step/tutorials/pt/tutorial3.step
/usr/share/step/tutorials/pt/tutorial4.step
/usr/share/step/tutorials/pt/tutorial5.step
/usr/share/step/tutorials/pt_BR/tutorial1.step
/usr/share/step/tutorials/pt_BR/tutorial2.step
/usr/share/step/tutorials/pt_BR/tutorial3.step
/usr/share/step/tutorials/pt_BR/tutorial4.step
/usr/share/step/tutorials/pt_BR/tutorial5.step
/usr/share/step/tutorials/ru/tutorial1.step
/usr/share/step/tutorials/ru/tutorial2.step
/usr/share/step/tutorials/ru/tutorial3.step
/usr/share/step/tutorials/ru/tutorial4.step
/usr/share/step/tutorials/ru/tutorial5.step
/usr/share/step/tutorials/sk/tutorial1.step
/usr/share/step/tutorials/sk/tutorial2.step
/usr/share/step/tutorials/sk/tutorial3.step
/usr/share/step/tutorials/sk/tutorial4.step
/usr/share/step/tutorials/sk/tutorial5.step
/usr/share/step/tutorials/tutorial1.step
/usr/share/step/tutorials/tutorial2.step
/usr/share/step/tutorials/tutorial3.step
/usr/share/step/tutorials/tutorial4.step
/usr/share/step/tutorials/tutorial5.step
/usr/share/step/tutorials/uk/tutorial1.step
/usr/share/step/tutorials/uk/tutorial2.step
/usr/share/step/tutorials/uk/tutorial3.step
/usr/share/step/tutorials/uk/tutorial4.step
/usr/share/step/tutorials/uk/tutorial5.step
/usr/share/step/tutorials/zh_TW/tutorial1.step
/usr/share/step/tutorials/zh_TW/tutorial2.step
/usr/share/step/tutorials/zh_TW/tutorial3.step
/usr/share/step/tutorials/zh_TW/tutorial4.step
/usr/share/step/tutorials/zh_TW/tutorial5.step
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
/usr/share/package-licenses/step/0c4be15f5177aafffe980ca09c0f4ca6ed741f43
/usr/share/package-licenses/step/40f6a79e31db3f532867ecebb7186eef8a34ff76
/usr/share/package-licenses/step/ff3ed70db4739b3c6747c7f624fe2bad70802987

%files locales -f step.lang -f step_example_files.lang -f step_objinfo_files.lang
%defattr(-,root,root,-)

