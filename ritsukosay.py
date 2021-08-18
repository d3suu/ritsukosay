#!/usr/bin/python3
import sys

# MIT License
#
# Copyright (c) 2021 Mateusz Dukat
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ASCII art was made using https://asciiart.club/ and sketch from Groundwork of EVANGELION Vol. 1 or 2
ritsuko = """
                                  »∞╓.⌐~─^  ª«▄ ▄e
                                ]æ            y. ═█º-▄
                           «Ö└7▀█ ╢            ▄ ▌▐    ▀
                        x"  ,   ║ `⌐           ║ ║ (    ▀▒▄
                       ∩ xº ╚"╤ ▐( ▌  ▌          ┤ ▐     `%  ºº-─~⌐
                       x  æV   ▌ ▒⌠▐  █       ▌ b│ ╡       ╙        ¥«▄
                     ┌█  Æ╓    █⌐▌∩╢  ▌▌      └ Ñ└ ∩        ▌           ""ⁿ«▄
                    ╓T⌐ ▀┌    ▀£▌█▓╝▄ ██     ▐ ¥b        ▐  ╣                b
                   ╓╬∩ É▒Ö   █┌╓╝ \ ▀▓  p    ▓ └         ▓             ▄▄▄,.  ¥
                   ╣█ ▓└█▓  ▒    █ !═█* ╫ ▐  █▄        ▒(░ ╒ ▌             ▒Ö╖ Y
                  (▀.▀ .╗█ ╓.f     (╫█Ñp▐ ▒▒ ▌▒    #  .▒▌( ▌ ▌              ▌ k▐
                   ▓▀  ▒╝▌┌█╒      ▐█-▓└ M▒█ M█.  (▌ ┌ ╗▌ ⌐█ ▒               ▌ █
                   ▀   █ ▌█▒∩ .⌐∞"ⁿ▀▄▄  ∩▒\▀ . ▓  Ñ ╒█ ▌█ ╓ p▌ `             ╙▒└╩▄
                         ██▀▒▄#æ▒p╔█▒▄  ⁿ ▄⌐▓  █ Γ└ƒ▓ ▐ ▀ █ ║▒   p           ▄▀╝N ▄
                         █▐ ▀╙ █▀████▄  ▐█"╙██▒▌╓─▀▓╝.─   ▒Y O    ¼  ╙       ▒QU' █
                          ▐   ⁿ"▓▀  ▀█▄  Ö   δ ▀█▌▓█ ▌   7  ╙      k  \      ▐ p  ▌
                         /      █   ╓██═(   U∩▐█ █ ║█        └▄     % ∩y      ▄└  ▒
                    ▄⌐^"       ▓▒─ª         ▐ ██▀ ▓  ╢▄       ▐▄     \| µ     ▐ ¥ ─
                 ▄                            █▌ ╣▀,╢█-╝▄      ▀▒     (        ▌ j
                  ½╖              ▓º          ║ /█▀██ ▒└▀█≥┐    Ö╕       └  {    ▐
                   └⌐                     ▀  .ÖQ"█╬▐∞¬╢  ╫  ▐▄  └ u       k ▐py ╘▐
                   (▄                         ╒  ▀  ▌-  ▄█  ▐ ▌  k p       φ ╘   ▓
                    ▀█▒                              └▄▄▄⌐▄"   t  ⌐ ,      ╙▄∩▒   ▀
                     ▀                          , « ╫█▄▄╧▌     ∩µ ╞ `▄      ╞ └ └▄ ▌
                                                ╒Ü▓▓▀▒   (¬ ⌐  ▐└  p ╙       ▒   ▐ ▐
                   ─                           Æ▒█▀   █  ╒█ B    k ▐  ▀     ,╙    ▌╫
                  ┘                          ╓Ö  ▀█▄╗██  ▐▐⌐▄   k ▄ h  ▌    ╠     ▐█
                 ╓                  .,⌐-  ▄∞Ö   ╓7 ▓- █  │ ▒M     ╘ ▌  ▐    Ñ  ∩▓  █
                 ╘▄   ~∞*^'""          ".      / ╡   ▐▐  ∩  ═    b µ█   ▒   ▌  {▓  ▌
                   "╬▀ⁿ«▄▄▄                   ,  Ö   █   .▄ ─(   . ▓▒▒  ╣   ▌  █▌▐ ▌
                            └. └º╖           6   ⌐─^╫██▌╠██( ╬B .▓ ▒▓ ▒ █M  █  ▀▒ ▌=
                                  V        ,~`W      █ ▌█└╣█▐.▌ ╬│▓ └  p▌├ ▐ ▒▓▐  ▀
                                       ,^  .ª          █  █▐∩ ▌▀  █    `▌ k╚ `Ñ
                                   à─" .∞"                █               └
                               ⌐^Ü  ,ⁿ    ┌"               █
                            «▄╣   ▄      /                 ▀
                            ½╙,%  ╫     # ⌐                ⌐▀█
                             b└⌐½ (⌐   ╒+            æ"▄ⁿ.▄▄∞▀ºº¬─╫
                              φ ▄∩ ▒   ▒ ∩        ▄O»æ▀T .         ▒
                               U└╣ C  ╙    ▄⌐e[åÑ*º"                ¥
                                ▓ ▌∩] .#æ╝^/                         ▒
                               ▄█ █a▌▀╙                               ▌
                           ▄∩▓█▌█#▌Ö       ,─*#"º╙└└.  .^*∞∞»▄\"\"\"\"\"^^*─▀««▄
"""

message = sys.argv[1:]
# Without arguments, print only Ritsuko
if len(message) == 0:
	print(ritsuko)
	quit()

# If message is longer than 40 characters, split it into lines
strMessage = " ".join(message)
newMessage = []
while len(strMessage) > 40:
	x = 40
	# From 40th character in strMessage, move back and check if character is space
	while len(strMessage) != 0:
		if " " not in strMessage:
			newMessage.append(strMessage)
			break
		if strMessage[x] == " ":
			# If it is, append it as new line, and remove this part from strMessage. Repeat.
			newMessage.append(strMessage[:x])
			strMessage = strMessage[x+1:]
			break
		else:
			x -= 1

# If strMessage is shorter than 40 characters, just append it
newMessage.append(strMessage)

# Split Ritsuko
ritsukoSplit = ritsuko.splitlines()

# Print full
print(" " + "_"*42 + " " + ritsukoSplit[0])
print("/" + " "*42 + "\\" + ritsukoSplit[1])
a = 2
for strMessage in newMessage:
	strLen = len(strMessage)
	print("| " + strMessage + " "*(40-strLen) + " |" + ritsukoSplit[a])
	a += 1
print("\\" + "_"*36 + " "*4 + "_"*2 + "/" + ritsukoSplit[a])
print(" "*37 + "\  |" + " "*3 + ritsukoSplit[a+1])
print(" "*37 + " \ |" + " "*3 + ritsukoSplit[a+2])
print(" "*37 + "  \|" + " "*3 + ritsukoSplit[a+3])
# ^I think this code is bad, Magi would be straight up mad for executing something like this

# Print rest of Ritsuko
for line in ritsukoSplit[a+4:]:
	print(" "*44 + line);
