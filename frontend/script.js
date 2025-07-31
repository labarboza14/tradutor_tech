async function traduzir() {
  const texto = document.getElementById("texto").value;

  document.getElementById("traduzido").innerText = "Traduzindo...";
  document.getElementById("simplificado").innerText = "";

  if (!texto.trim()) {
    document.getElementById("traduzido").innerText = "Por favor, insira um texto para traduzir.";
    return;
  }

  try {
    const resposta = await fetch("http://127.0.0.1:8000/traduzir", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ conteudo: texto })
    });

    if (!resposta.ok) {
      throw new Error("Erro na resposta da API");
    }

    const resultado = await resposta.json();

    if (resultado.erro) {
      document.getElementById("traduzido").innerText = resultado.erro;
      document.getElementById("simplificado").innerText = "";
      return;
    }

    document.getElementById("traduzido").innerText = resultado.traduzido;
    document.getElementById("simplificado").innerText = resultado.simplificado;

  } catch (erro) {
    console.error(erro);
    document.getElementById("traduzido").innerText = "Ocorreu um erro ao tentar traduzir.";
    document.getElementById("simplificado").innerText = "";
  }
}
