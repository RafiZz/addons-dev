# -*- coding: utf-8 -*-
# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import models, api, exceptions, _
from odoo.addons.openapi.controllers import pinguin


class IrExports(models.Model):
    _inherit = 'ir.exports'

    @api.constrains('resource', 'export_fields')
    def _check_fields(self):
        # this exports record used in openapi.access
        if not self.env['openapi.access'].search_count(
            ['|', ('read_one_id', '=', self.id), ('read_many_id', '=', self.id)]
        ):
            return True

        fields = self.export_fields.mapped('name')
        for field in fields:
            if fields.count(field) > 1:
                raise exceptions.ValidationError(
                    _('exported "%s" field duplicated.') % field)

        fields.sort()
        for i in range(len(fields) - 1):
            if fields[i+1].startswith(fields[i]) and\
                    '/' in fields[i+1].replace(fields[i], ''):
                raise exceptions.ValidationError(
                    _('You must delete the "%s" field or "%s" field') % (fields[i], fields[i+1])
                )

        # Model = self.env[self.resource].search([], limit=1)
        # print(pinguin.get_dict_from_record(Model, fields, (), ()))
