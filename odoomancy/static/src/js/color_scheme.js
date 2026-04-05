/** @odoo-module **/

import { registry } from "@web/core/registry";
import { cookie } from "@web/core/browser/cookie";
import { session } from "@web/session";
import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";

function applyTheme(scheme) {
    document.body.classList.remove("odoomancy-dark", "odoomancy-light");
    // If scheme is missing or explicitly 'default', use Odoo core theme
    if (!scheme || scheme === "default") {
        cookie.delete("color_scheme");
        return;
    }
    // For 'light' or 'dark', apply odoomancy classes and persist choice
    document.body.classList.add(`odoomancy-${scheme}`);
    cookie.set("color_scheme", scheme);
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
        const stored = cookie.get("color_scheme");
        const scheme = session.color_scheme || (stored ? stored : "default");
        applyTheme(scheme);
    },
});