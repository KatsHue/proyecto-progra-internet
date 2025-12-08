import { Link } from "react-router-dom";

export default function Logo() {
  return (
    <Link to="/" className="flex justify-center">
      <img
        src="/assets/logo2-1.png"
        alt="LogoTipo"
        className="w-20 h-auto mx-auto cursor-pointer hover:opacity-80 transition"
      />
    </Link>
  );
}
