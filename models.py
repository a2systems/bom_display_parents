from odoo import tools, models, fields, api, _

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    def _compute_used_in_bom_text(self):
        for rec in self:
            res = ''
            if rec.used_in_bom_count > 0:
                res = '<p>This BoM is used in:</p><ul>'
                product_id = self.env['product.product'].search([('product_tmpl_id','=',rec.product_tmpl_id.id)],limit=1)
                bom_lines = self.env['mrp.bom.line'].search([('product_id','=',product_id.id)])
                for bom_line in bom_lines:
                    res = res + '<li> ' + bom_line.bom_id.display_name + ' </li>'
                res = res + '</ul>'
            rec.used_in_bom_text = res

    used_in_bom_count = fields.Integer('Used in BoM Count',related='product_tmpl_id.used_in_bom_count')
    used_in_bom_text = fields.Text('Used in BoM Text',compute=_compute_used_in_bom_text)

