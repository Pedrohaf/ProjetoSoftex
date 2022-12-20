import React from "react";
import { Route, BrowserRouter } from "react-router-dom";

import Home from "./Home";
import empresas from "./pages/empresa";
import contato from "./pages/contato";

export default function Routes () {
   return(
       <BrowserRouter>
           <Route component = { Home }  path="/" exact />
           <Route component = { empresas }  path="/empresas" />
           <Route component = { contato }  path="/contatos" />
       </BrowserRouter>
   )
}

