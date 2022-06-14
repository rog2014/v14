# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import calendar
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero

class AccountAsset(models.Model):
    _inherit = 'account.asset'

    employee_id = fields.Many2one("hr.employee","Employee Responsible")
    deaprtment_id = fields.Many2one("hr.department","Department ")
    serian_no = fields.Char("S/N")

    
        
    
    
    
    

    
    
