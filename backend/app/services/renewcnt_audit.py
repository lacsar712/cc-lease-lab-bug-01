"""续约次数列写反读轨审计。"""
from __future__ import annotations

from app.services import renewcnt as core
from app.services import renewcnt_cutover as cutover
from app.services import renewcnt_dualwrite as dual


def audit_summary() -> dict:
    return {
        "title": "续约次数列写反审计",
        "core": core.dashboard(),
        "cutover": cutover.board(),
        "dualwrite": dual.dual_board(),
        "half": core.half_fix_display(),
    }
