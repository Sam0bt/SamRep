 #!/bin/bash

[ $UID = 0 ] && { echo "Lütfen Root Kullanıcısı Dışında Başka Bir Kullanıcı Ile Scripti Çalıştırın. Kullanıcılarınız: $(ls /home)" ; exit 1 ; }

set -e
set -o pipefail

tmp=$(mktemp)
curl -sSLf https://github.com/emojione/emojione-assets/releases/download/4.5/emojione-android.ttf > "$tmp"


echo "SHA Kontrol: TAMAM"
sha256=5a8ec97548326235f427dff60749bdbd525de20383c42b1ae73f3bae883f58c2
echo "$sha256 $tmp" | sha256sum --check --status
echo "SHA: TAMAM"

mkdir -p ~/.local/share/fonts/
mv "$tmp" ~/.local/share/fonts/emojione-android.ttf

echo "FONT Ayarları: TAMAM"
mkdir -p ~/.config/fontconfig/conf.d
echo '<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>

  <!-- Add emoji generic family -->
  <alias binding="strong">
    <family>emoji</family>
    <default><family>Emoji One</family></default>
  </alias>

  <!-- Aliases for the other emoji fonts -->
  <alias binding="strong">
    <family>Apple Color Emoji</family>
    <prefer><family>Emoji One</family></prefer>
  </alias>
  <alias binding="strong">
    <family>Segoe UI Emoji</family>
    <prefer><family>Emoji One</family></prefer>
  </alias>
  <alias binding="strong">
    <family>Noto Color Emoji</family>
    <prefer><family>Emoji One</family></prefer>
  </alias>

  <!-- Do not allow any app to use Symbola, ever -->
  <selectfont>
    <rejectfont>
      <pattern>
        <patelt name="family">
          <string>Symbola</string>
        </patelt>
      </pattern>
    </rejectfont>
  </selectfont>
</fontconfig>
' > ~/.config/fontconfig/conf.d/70-emojione-color.conf

fc-cache -f

echo "Hadi iyisiniz. Alırım bi ARO :)"
