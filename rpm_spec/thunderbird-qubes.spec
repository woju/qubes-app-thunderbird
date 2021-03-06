#
# The Qubes OS Project, http://www.qubes-os.org
#
# Copyright (C) 2011  Marek Marczykowski <marmarek@invisiblethingslab.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#


%{!?version: %define version %(cat version)}

%define extdir %{_libdir}/mozilla/extensions/{3550f703-e582-4d05-9a08-453d09bdfdc6}/qubes-attachment@qubes-os.org

Name:		thunderbird-qubes
Version:	%{version}
Release:	1%{dist}
Summary:	The Qubes extension for Thunderbird

Group:		Qubes
Vendor:		Invisible Things Lab
License:	GPL
URL:		http://www.qubes-os.org

Requires:	thunderbird

%define _builddir %(pwd)

%description
The Qubes email attachments actions for Thunderbird.

%prep
# we operate on the current directory, so no need to unpack anything

%build
make install.rdf

%install
rm -rf $RPM_BUILD_ROOT
make install-vm DESTDIR=$RPM_BUILD_ROOT EXTDIR=%{extdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{extdir}
%{extdir}/chrome.manifest
%{extdir}/install.rdf
%{extdir}/chrome/locale/en-US/qubesattachment.dtd
%{extdir}/chrome/content/options.xul
%{extdir}/chrome/content/qubesattachment.js
%{extdir}/chrome/content/msgHdrViewOverlay.xul
%{extdir}/chrome/skin/qubesattachment.css
%{extdir}/defaults/preferences/prefs.js
