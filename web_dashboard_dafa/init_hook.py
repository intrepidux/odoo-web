# Copyright 2016-2019 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID
from odoo.api import Environment


def post_init_hook(cr, _):
    with Environment.manage():
        env = Environment(cr, SUPERUSER_ID, {})
        users = env['res.users'].search([])
        for user in users:
            env['af.dashboard'].create({
                'name': user.name,
                'user_id': user.id
            })
