from openerp.osv import fields,osv
from openerp import tools

 
class sale_order_report(osv.osv):
    _name = "sale.order.report"
    _description = "Sale Order Report"
    _auto = False
    _columns = {
	'user_id': fields.many2one('res.users','Vendedor'),
	'product_id': fields.many2one('product.product','Product'),
	'section_id': fields.many2one('crm.case.section','Sucursal'),
	'price_subtotal': fields.float('Total',readonly=True,group_operator="sum",digits=(16,2)), 
	'product_uom_qty': fields.float('Quantity',readonly=True,group_operator="sum",digits=(16,2)),
	}
 
    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'sale_order_report')
	cr.execute("""
		create or replace view sale_order_report as (
			select  b.id as id,b.product_id,a.section_id,a.user_id,b.price_unit * b.product_uom_qty as price_subtotal,b.product_uom_qty  
                        from sale_order a inner join sale_order_line b on a.id = b.order_id where a.state in ('manual','progress'))
	""")	
 
sale_order_report()
