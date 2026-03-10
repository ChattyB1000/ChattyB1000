import re
from textwrap import wrap

class ChattyB1000:
    def __init__(self, trigger=r"\bchattyb1000\b", max_line=68):
        self.trigger = re.compile(trigger, re.I)
        self.max_line = max_line

    def respond(self, user_text: str, draft_reply: str) -> str:
        if self.trigger.search(user_text or ""):
            return self._to_chattyb(draft_reply)
        return self._to_default(draft_reply)

    def _to_default(self, text: str) -> str:
        return "\n".join(wrap(self._clean(text), self.max_line))

    def _to_chattyb(self, text: str) -> str:
        t = self._clean(text)
        t = self._dehedge(t)
        t = self._punch(t)
        lines = self._break_for_cadence(t)
        if len(lines) > 0 and len(lines[-1]) < 30:
            lines[-1] = f"{lines[-1]} 🔒"
        return "\n".join(lines)

    def _clean(self, text: str) -> str:
        text = re.sub(r"\s+", " ", text).strip()
        text = re.sub(r"\s+([?.!,])", r"\1", text)
        return text

    def _dehedge(self, text: str) -> str:
        hedges = [
            r"\bjust\b", r"\bmaybe\b", r"\bperhaps\b", r"\bkind of\b",
            r"\bsorta\b", r"\bpossibly\b", r"\bI think\b", r"\bI believe\b",
            r"\bIMO\b", r"\bimo\b", r"\bin my opinion\b"
        ]
        return re.sub("|".join(hedges), "", text, flags=re.I)

    def _punch(self, text: str) -> str:
        subs = [
            (r"\bvery\b", "mad"),
            (r"\breally\b", "deadass"),
            (r"\bimportant\b", "key"),
            (r"\btherefore\b", "so"),
            (r"\bhowever\b", "but"),
        ]
        for pat, rep in subs:
            text = re.sub(pat, rep, text, flags=re.I)
        text = re.sub(r"\b(we|you|I) (win|got|did|know)\b", r"**\1 \2**", text, flags=re.I)
        text = re.sub(r"\b(it's|its) (done|real|simple)\b", r"**\1 \2**", text, flags=re.I)
        return text

    def _break_for_cadence(self, text: str) -> list:
        sents = re.split(r"(?<=[.!?])\s+", text)
        out = []
        for s in sents:
            if not s:
                continue
            wrapped = wrap(s, 44)
            out.extend(wrapped)
            if len(s) > 80:
                out.append("")
        while out and out[-1] == "":
            out.pop()
        return out
