/** @odoo-module **/

import { registry } from "@web/core/registry";
import { cookie } from "@web/core/browser/cookie";
import { session } from "@web/session";
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";

function applyTheme(scheme) {
    document.body.classList.remove("odoomancy-dark", "odoomancy-light");
    document.body.classList.add(`odoomancy-${scheme || "light"}`);
    cookie.set("color_scheme", scheme || "light");
}

// Parchear el FormController para detectar cuando se guarda res.users
patch(FormController.prototype, {
    async saveButtonClicked(params) {
        await super.saveButtonClicked(params);
        if (this.model.root.resModel === "res.users") {
            const colorScheme = this.model.root.data.color_scheme;
            if (colorScheme) {
                applyTheme(colorScheme);
            }
        }
    },
});

registry.category("services").add("odoomancy_color_scheme", {
    start() {
        const scheme = session.color_scheme || cookie.get("color_scheme") || "light";
        applyTheme(scheme);
    },
});