using System.Security.Claims;

namespace Nexus.Security;

public sealed class AuthorizationService
{
    public bool CanReprocess(ClaimsPrincipal principal)
    {
        return principal.IsInRole("Operator") ||
               principal.IsInRole("Administrator");
    }

    public bool CanRead(ClaimsPrincipal principal, string tenantId)
    {
        var claim = principal.FindFirst("tenant_id");
        return claim?.Value == tenantId;
    }
}
