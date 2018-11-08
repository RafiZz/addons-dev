# -*- coding: utf-8 -*-
# Copyright 2018 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import models, fields, api, tools, http


class IrModel(models.Model):
    _inherit = 'ir.model'

    api_access_ids = fields.One2many('openapi.access', 'model_id', 'Access via API')


# class IrModelAccess(models.Model):
#     _inherit = 'ir.model.access'
#
#     @api.model
#     @tools.ormcache_context('self._uid', 'model', 'mode', 'raise_exception', keys=('lang',))
#     def check(self, model, mode='read', raise_exception=True):
#         if isinstance(model, models.BaseModel):
#             assert model._name == 'ir.model', 'Invalid model object'
#             model_name = model.model
#         else:
#             model_name = model
#         print(model_name)
#         print(self.env.__dict__)
#
#         return super(IrModelAccess, self).check(model=model, mode=mode, raise_exception=raise_exception)
