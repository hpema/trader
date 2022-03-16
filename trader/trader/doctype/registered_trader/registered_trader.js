// Copyright (c) 2021, Hemant Pema and contributors
// For license information, please see license.txt

frappe.ui.form.on('Registered Trader', {
	refresh: function(frm) {
		frm.add_custom_button(__('Generate Key'), function(){
			frappe.call({
				method: 'trader.trader.doctype.registered_trader.registered_trader.generate_key',
				args: {},
				callback: function (r){
					console.log(r);
				}
			});
		}, __("Utilities"));
	}
	
});
