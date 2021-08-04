<template>
  <v-row justify="center">
      <v-dialog
        v-model="dialogVisible"
        persistent
        max-width="300"
      >
        <v-card>
            <v-card-title class="text-h6">
                {{ text }}
            </v-card-title>
            <v-card-actions>
                <v-btn
                    @click="onConfirm"
                    color="success"
                >Да</v-btn>
                <v-spacer></v-spacer>
                <v-btn
                    @click="onCancel"
                    color="primary"
                >Нет</v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>
  </v-row>
</template>

<script>
export default {
    data: () => ({
        dialogVisible: false
    }),
    props: {
        text: {
            required: true,
            type: String
        },
        value: {
            type: Boolean,
            default: false
        }
    },
    created() {
        this.dialogVisible = this.value;
    },
    methods: {
        onConfirm() {
            this.$emit("confrim");
        },
        onCancel() {
            this.$emit("cancel");
        }
    },
    watch: {
        value(newValue) {
            this.dialogVisible = newValue;
        },
        dialogVisible(newValue) {
            this.$emit("input", newValue);
        }
    }
}
</script>