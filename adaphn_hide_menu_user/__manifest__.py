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

{
    'name': 'Ocultar menu a nivel de usuario',
    'version': '14.0.1.0.0',
    'summary': 'Ocultar menu nivel de usuario odoo',
    'description': 'Hide Any Menu Item User Wise, Hide Menu Items, Hide Menu',
    'author': 'Grupo ADAP',
    'company': 'Grupo ADAP',
    'maintainer': 'Grupo ADAP Solutions tools',
    'website': "https://www.grupoadap.com",
    'depends': ['base'],
    'data': [
        'views/res_users.xml',
        'security/security.xml'
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
