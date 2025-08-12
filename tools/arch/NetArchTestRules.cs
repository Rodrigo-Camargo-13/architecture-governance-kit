using NetArchTest.Rules;
using Xunit;

namespace ArchitectureGovernanceKit.ArchitectureTests
{
    public class ArchitectureRules
    {
        [Fact]
        public void Domain_nao_pode_referenciar_infra_ou_api()
        {
            var result = Types
                .InCurrentDomain()
                .That()
                .ResideInNamespace("*.Domain")
                .ShouldNot()
                .HaveDependencyOnAny("*.Infrastructure", "*.Api")
                .GetResult();

            Assert.True(result.IsSuccessful, string.Join("\n", result.FailingTypeNames));
        }

        [Fact]
        public void Application_nao_pode_dependender_de_Api()
        {
            var result = Types
                .InCurrentDomain()
                .That()
                .ResideInNamespace("*.Application")
                .ShouldNot()
                .HaveDependencyOnAny("*.Api")
                .GetResult();

            Assert.True(result.IsSuccessful, string.Join("\n", result.FailingTypeNames));
        }
    }
}
