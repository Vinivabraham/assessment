from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_charge = fields.Float(string='Delivery Charge')

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        product_ids = self.env['product.product'].search([('name', '=', 'Delivery Charge')])
        if not product_ids:
            product_ids = self.env['product.product'].create({
                'name': 'Delivery Charge',
                'detailed_type': 'service',
                'invoice_policy': 'order'
            })
        if res.delivery_charge and res.order_line.product_id:
            res.order_line.create({
                'product_id': product_ids.id or False,
                'name': 'Delivery Charge' or '',
                'product_uom_qty': 1.0,
                'product_uom': 1,
                'price_unit': res.delivery_charge,
                'order_id': res.id,
                'tax_id': False,
                'is_delivery_charge': True
            })

        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_delivery_charge = fields.Boolean(string='Delivery Charge')


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    is_delivery_charge = fields.Boolean(string='Delivery Charge')

    def create(self, vals_list):
        res = super(AccountMoveLine, self).create(vals_list)
        for rec in res:
            if rec.product_id.name == 'Delivery Charge':
                rec.is_delivery_charge = True
        return res
