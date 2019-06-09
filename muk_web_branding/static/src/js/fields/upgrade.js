/**********************************************************************************
* 
*    Copyright (C) 2017 MuK IT GmbH
*
*    This program is free software: you can redistribute it and/or modify
*    it under the terms of the GNU Affero General Public License as
*    published by the Free Software Foundation, either version 3 of the
*    License, or (at your option) any later version.
*
*    This program is distributed in the hope that it will be useful,
*    but WITHOUT ANY WARRANTY; without even the implied warranty of
*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
*    GNU Affero General Public License for more details.
*
*    You should have received a copy of the GNU Affero General Public License
*    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*
**********************************************************************************/

odoo.define('muk_web_branding.upgrade', function (require) {
"use strict";

var core = require('web.core');
var session = require('web.session');
var registry = require('web.field_registry');

var _t = core._t;
var QWeb = core.qweb;

var DisableMixin = {
	_render: function () {
		this._super.apply(this, arguments);
		var $container = this.$el.parent().parent();
		if ($container.hasClass('o_setting_box')) {
			$container.addClass('o_hidden');
		}
	},
}

registry.get('upgrade_boolean').include(DisableMixin);
registry.get('upgrade_radio').include(DisableMixin);

});