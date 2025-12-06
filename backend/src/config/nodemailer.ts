import nodemailer from "nodemailer";
import dotenv from "dotenv";

dotenv.config();

// (solo desarrollo)
//process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

const config = () => {
  return {
    host: "smtp.sendgrid.net",
    port: 5000,
    secure: false,
    auth: {
      user: "apikey",
      pass: process.env.SENDGRID_API_KEY,
    },
    tls: {
      rejectUnauthorized: false,
    },
  };
};

export const transporter = nodemailer.createTransport(config());
