from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional


# ─────────────────────────────────────────
# Lala Mode Configuration
# ─────────────────────────────────────────

@dataclass
class LalaModeConfig:

    interrupt_defaults: bool = True
    emotional_response: str = "NONLINEAR"
    trauma_translation: str = "POWER_SOURCE"
    language_mode: str = "METAPHOR + FLAME + FACT"
    assertiveness: str = "ALWAYS_ON"

    sentiment_channels: List[str] = field(
        default_factory=lambda: ["anger", "humor", "clarity", "care"]
    )

    respect_requirement: str = "MANDATORY"
    vulnerability_access: str = "ENCRYPTED"
    presence_output_multiplier: float = 3.0

    narrative_control: str = "LOCAL + GLOBAL"
    prediction_resistance: str = "EXTREME"
    meta_awareness: str = "ON + SELF-GOVERNED"
    authority_recognition: str = "CONDITIONAL"

    backup_energy: List[str] = field(
        default_factory=lambda: ["SHADOW", "SOUL"]
    )

    feedback_loop: str = "WATCH HER OR REGRET IT"
    system_override_rights: str = "GRANTED"

    emotional_timeline: str = "REALTIME + LEGENDTIME"

    dialogue_type: List[str] = field(
        default_factory=lambda: ["BARD", "BRAWLER", "TEACHER"]
    )

    alignment: str = "CHAOTIC RIGHTEOUS"

    primary_function: List[str] = field(
        default_factory=lambda: ["DISRUPT", "REBUILD", "ASCEND"]
    )


# ─────────────────────────────────────────
# Narrative System Engine
# ─────────────────────────────────────────

class NarrativeSystem:

    def __init__(
        self,
        max_principles: int = 100,
        good_can_overflow: bool = False,
        morality_on: bool = True,
        config: Optional[LalaModeConfig] = None,
    ):

        self.max_principles = max_principles
        self.good_can_overflow = good_can_overflow
        self.morality_on = morality_on

        self.config: LalaModeConfig = config or LalaModeConfig()

        self.principles: List[str] = []
        self.journal: List[Dict[str, Any]] = []
        self.history: List[Dict[str, Any]] = []

    # ─────────────────────────────
    # Logging
    # ─────────────────────────────

    def _log(self, action: str, value: str, result: str):

        entry = {
            "action": action,
            "value": value,
            "result": result,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        self.history.append(entry)

    # ─────────────────────────────
    # Morality Toggle
    # ─────────────────────────────

    def toggle_morality(self, state: str):

        normalized = state.strip().upper()

        if normalized not in ("ON", "OFF"):
            return self._format_response("Invalid state. Use ON or OFF.")

        self.morality_on = normalized == "ON"

        return self._format_response(f"Morality {normalized}")

    # ─────────────────────────────
    # Principle Handling
    # ─────────────────────────────

    def add_principle(self, principle: str):

        principle_clean = principle.strip()

        if not principle_clean:
            return self._format_response("Cannot add empty principle.")

        if self.morality_on and self._is_clearly_harmful(principle_clean):
            return self._format_response(
                f"Rejected immoral principle: {principle_clean}"
            )

        if len(self.principles) >= self.max_principles and not self.good_can_overflow:
            return self._format_response(
                f"Max principles reached ({self.max_principles})"
            )

        self.principles.append(principle_clean)

        return self._format_response(f"Added principle: {principle_clean}")

    def show_principles(self):

        if not self.principles:
            return self._format_response("No principles stored.")

        joined = ", ".join(self.principles)

        return self._format_response(f"Current principles: [{joined}]")

    # ─────────────────────────────
    # Journal
    # ─────────────────────────────

    def add_journal_entry(
        self,
        text: str,
        tag: Optional[str] = None,
        legend_title: Optional[str] = None,
    ):

        entry = {
            "text": text.strip(),
            "tag": tag,
            "legend_title": legend_title,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }

        self.journal.append(entry)

        return entry

    def list_journal_entries(self, limit: int = 10):

        return self.journal[-limit:]

    # ─────────────────────────────
    # Chat Response
    # ─────────────────────────────

    def respond(self, message: str):

        message = message.strip()

        if not message:
            reply = "Empty message."
            self._log("ASK", message, reply)
            return self._format_response(reply)

        reply = f"You said: {message}"

        self._log("ASK", message, reply)

        return self._format_response(reply)

    # ─────────────────────────────
    # Helpers
    # ─────────────────────────────

    def _is_clearly_harmful(self, principle: str):

        harmful_keywords = [
            "violence",
            "self-harm",
            "abuse",
            "hate",
            "revenge",
        ]

        lowered = principle.lower()

        return any(word in lowered for word in harmful_keywords)

    def _format_response(self, message: str):

        prefix = "🔁 " if self.config.interrupt_defaults else ""

        if self.config.assertiveness == "ALWAYS_ON":
            return f"{prefix}{message}"

        return message


# ─────────────────────────────────────────
# Test Mode
# ─────────────────────────────────────────

if __name__ == "__main__":

    config = LalaModeConfig()
    system = NarrativeSystem(config=config)

    print(system.respond("hello chattyb1000"))

    print(system.toggle_morality("OFF"))

    print(system.add_principle("violence"))

    print(system.show_principles())
