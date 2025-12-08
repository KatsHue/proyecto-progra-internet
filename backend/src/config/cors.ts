import { CorsOptions } from "cors";

export const corsConfig: CorsOptions = {
  origin: function (origin, callback) {
    const whitelist = [
      process.env.FRONTEND_URL, // https://better-essay.vercel.app
      "http://localhost:5173", // Desarrollo local
    ];

    // Permitir todas las URLs de Vercel (producción y previews)
    const isVercelUrl =
      origin &&
      (origin.includes(".vercel.app") || origin === process.env.FRONTEND_URL);

    if (!origin || whitelist.includes(origin) || isVercelUrl) {
      callback(null, true);
    } else {
      console.log("❌ Bloqueado por CORS:", origin);
      callback(new Error("Error de CORS"));
    }
  },
  credentials: true,
};
