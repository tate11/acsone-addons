# -*- coding: utf-8 -*-
##############################################################################
#
#    Authors: Nemry Jonathan & Laurent Mignon
#    Copyright (c) 2014 Acsone SA/NV (http://www.acsone.eu)
#    All Rights Reserved
#
#    WARNING: This program as such is intended to be used by professional
#    programmers who take the whole responsibility of assessing all potential
#    consequences resulting from its eventual inadequacies and bugs.
#    End users who are looking for a ready-to-use solution with commercial
#    guarantees and support are strongly advised to contact a Free Software
#    Service Company.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import openerp

try:
    if openerp.release.version_info[0] > 7 or (openerp.release.version_info[0] == 7 and
                                               openerp.release.version_info[1] > 'saas~2'):
        from . import controllers
        from . import models
        from . import ir_mail_server
except:
    import logging
    _logger = logging.getLogger(__name__)
    _logger.warning("This module is incompatible with current version of OE server: %s" % openerp.release.version)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: