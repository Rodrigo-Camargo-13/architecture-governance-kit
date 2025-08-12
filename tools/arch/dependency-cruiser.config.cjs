/** @type {import('dependency-cruiser').IConfiguration} */
module.exports = {
  forbidden: [
    { name: "no-circular", severity: "error", from: {}, to: { circular: true } },
    {
      name: "domain-boundaries",
      comment: "Domínio não deve depender de camadas externas.",
      severity: "warn",
      from: { path: "^src/domain" },
      to: { path: "^src/(infra|adapters|ui)" }
    }
  ],
  options: {
    doNotFollow: { path: "node_modules" },
    tsConfig: { fileName: "tsconfig.json" },
    combinedDependencies: true
  }
};
