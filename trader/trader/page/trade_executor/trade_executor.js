frappe.pages["trade-executor"].on_page_load = function (wrapper) {
	frappe.ui.make_app_page({
		parent: wrapper,
		title: __("Trade Executor"),
		single_column: true,
	});
};

frappe.pages["trade-executor"].on_page_show = function (wrapper) {
	load_desk_page(wrapper);
};

function load_desk_page(wrapper) {
	let $parent = $(wrapper).find(".layout-main-section");
	$parent.empty();

	frappe.require("trade_executor.bundle.js").then(() => {
		frappe.trade_executor = new frappe.ui.TradeExecutor({
			wrapper: $parent,
			page: wrapper.page,
		});
	});
}