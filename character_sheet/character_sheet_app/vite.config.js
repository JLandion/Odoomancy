import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react-swc";

export default defineConfig(({ mode }) => {
  // Load environment variables based on the mode
  const env = loadEnv(mode, process.cwd(), "");

  // Set the base path based on the environment
  const base =
    mode === "development"
      ? "/web/character-sheet/api/app"
      : "/character_sheet/static/character-sheet-app";

  return {
    plugins: [react()],
    base,
    build: {
      chunkSizeWarningLimit: 750,
    },
    test: {
      globals: true, // allows use of describe/it/expect in test files without importing them
      environment: 'jsdom',
      setupFiles: './src/tests/setupTests.js',
      clearMocks: true, // automatically clear mock calls and instances between every test
    },
  };
});