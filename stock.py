from openerp.osv import fields,osv
from openerp import tools

 
class stock_picking_report(osv.osv):
    _name = "stock.picking.report"
    _description = "Stock Picking Report"
    _auto = False
    _columns = {
	'state': fields.char('State'),
	'date': fields.datetime('Date'),
	'date_done': fields.datetime('Date Done'),
	'partner_id': fields.many2one('res.partner','Partner'),
	'move_type': fields.char('Move Type'),
	'picking_type_id': fields.many2one('stock.picking.type','Picking Type'),
	'product_id': fields.many2one('product.product','Product'),
	'product_uom_qty': fields.float('Quantity',readonly=True,group_operator="sum",digits=(16,2)),
	'location_id': fields.many2one('stock.location','Source Location'),
	'location_dest_id': fields.many2one('stock.location','Destination Location'),
	'familia': fields.many2one('product.familia','Familia'),
	'categoria': fields.many2one('product.categoria','Categoria'),
	'subcategoria': fields.many2one('product.subcategoria','Sub-Categoria'),
	'version': fields.many2one('product.version','Version'),
	}
 
    def init(self, cr):
        tools.sql.drop_view_if_exists(cr, 'stock_picking_report')
	cr.execute("""
		create or replace view stock_picking_report as (
select sm.id,sp.state,sp.date,sp.date_done,sp.partner_id,sp.move_type,sp.picking_type_id,sm.product_id,sm.product_uom_qty,sm.location_id,sm.location_dest_id,pp.familia,pp.categoria,pp.subcategoria,pp.version from stock_picking sp inner join stock_move sm on sp.id = picking_id inner join product_product pp on pp.id = sm.product_id)
	""")	
 
stock_picking_report()
