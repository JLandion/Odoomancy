/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { useService } from "@web/core/utils/hooks";
import { onMounted, onWillUnmount } from "@odoo/owl";

patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
        this._orm = useService("orm");
        this._pollingTimer = null;

        onMounted(() => {
            const isRunning = this.model.root.data?.is_running;
            if (isRunning) this._startPolling();
        });

        onWillUnmount(() => {
            this._stopPolling();
        });
    },

    _startPolling() {
        if (this._pollingTimer) return;
        this._pollingTimer = setInterval(() => this._poll(), 2000);
    },

    _stopPolling() {
        if (this._pollingTimer) {
            clearInterval(this._pollingTimer);
            this._pollingTimer = null;
        }
    },

    async _poll() {
        const resId = this.model.root.resId;
        const resModel = this.model.root.resModel;
        if (!resId || !resModel) return;
        if (!resModel.startsWith("odoomancy")) return;

        try {
            const result = await this._orm.call(
                resModel,
                "action_get_progress",
                [[resId]]
            );

            if (!result) return;

            await this.model.root.load();
            this.model.notify();

            if (!result.is_running) this._stopPolling();

        } catch (e) {
            console.error("[odoomancy] Polling error:", e);
            this._stopPolling();
        }
    },

    async executeAction(action) {
        const result = await super.executeAction(...arguments);
        if (action?.name === "action_import") {
            setTimeout(() => this._startPolling(), 1000);
        }
        return result;
    },
});