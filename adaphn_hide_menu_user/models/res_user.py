# -*- coding: utf-8 -*-
#############################################################################
#
#    Grupo ADAP S.A.
#
#    Copyright (C) 2012-TODAY Grupo ADAP S.A.(<https://www.grupoadap.com>)
#    Author: Grupo ADAP S.A. Solutions Tools(<https://www.grupoadap.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

from odoo import models, fields, api


class HideMenuUser(models.Model):
    _inherit = 'res.users'

    @api.model
    def create(self, vals):
        """
        De lo contrario, el menú seguirá oculto incluso después de eliminarlo de la lista
        """
        self.clear_caches()
        return super(HideMenuUser, self).create(vals)

    def write(self, vals):
        """
       De lo contrario, el menú seguirá oculto incluso después de eliminarlo de la lista
        """
        res = super(HideMenuUser, self).write(vals)
        for menu in self.hide_menu_ids:
            menu.write({
                'restrict_user_ids': [(4, self.id)]
            })
        self.clear_caches()
        return res

    def _get_is_admin(self):
        """
        la pestaña Ocultar menú específico se ocultará para el formulario de usuario Administrador.
        De lo contrario, una vez que el menú esté oculto, será difícil volver a habilitarlo.
        """
        for rec in self:
            rec.is_admin = False
            if rec.id == self.env.ref('base.user_admin').id:
                rec.is_admin = True

    hide_menu_ids = fields.Many2many('ir.ui.menu', string="Menu", store=True,
                                     help='Seleccione los elementos del menú que deben ser '
                                          'Oculto a este usuario ')
    is_admin = fields.Boolean(compute=_get_is_admin)


class RestrictMenu(models.Model):
    _inherit = 'ir.ui.menu'

    restrict_user_ids = fields.Many2many('res.users')
