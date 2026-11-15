# Langkah manual: `009 - A new project from the foundation`

Langkah yang butuh mata, tangan, akun, perangkat, atau izin kamu. Tidak ada sesi yang menjalankannya. Kirim hasilnya ke lead (ID langkah, `PASS` atau `FAIL`, dan output bila `FAIL`); lead meneruskannya ke checker yang mencentang `verify.md`. `FAIL` membuka kembali kotaknya.

Keputusan yang diambil atas namamu ada di `009 - A new project from the foundation.log.md` bagian "Keputusan delegasi"; baris bertanda `berat` paling perlu kamu baca. Untuk membatalkan satu baris, sebut barisnya ke lead.

## Ringkasan

| ID | Langkah | AC | Kotak yang dicentang dengan langkah ini `NOT_RUN` | Bisa dijalankan sesudah | Hasil |
| --- | --- | --- | --- | --- | --- |
| `F009-1` | Xcode menampilkan `Identity.xcconfig` di daftar file dan tidak ada target yang memakainya sebagai base config | spec 0003 AC-1 | milestone 1 (sudah `[x]`), `Build it`, `Verify it` | sekarang, di `main` | `NOT_RUN` |
| `F009-2` | Halaman Actions menawarkan checkbox `derived` yang mati secara bawaan | spec 0003 AC-10 | milestone 3, `Build it`, `Verify it` | sekarang, `origin/main` memuat `4a153fe` | `NOT_RUN` |

## Nilai dari user

Nilai yang hanya kamu tahu. AC di kolom ketiga `BLOCKED` sampai nilainya ada.

| ID | Nilai yang dibutuhkan | AC yang menunggu | File yang menunggu |
| --- | --- | --- | --- |

Belum ada.

## Fitur `009`: `A new project from the foundation` (spec `0003`)

### `F009-1` · Xcode menampilkan `Identity.xcconfig`

Dari laporan `chk-f009-verify` (2026-11-15). Membuktikan spec 0003 AC-1.

- **Prasyarat:** Xcode 27.1, checkout `main`.
- **Jalankan:** buka `apps/ios/MobileFoundation.xcodeproj` di Xcode dan lihat daftar file serta tab Info proyek, bagian Configurations.
- **Lulus bila:** `Identity.xcconfig` terlihat di daftar file di samping `App.xcconfig`, dan tidak ada target yang memakainya sebagai base config.
- **Hanya langkah ini yang bisa membuktikan:** tampilan Xcode itu sendiri. Bukti pengganti sudah lulus: `project.pbxproj` memuat file reference `Identity.xcconfig` di grup yang sama tepat sesudah `App.xcconfig`, dan keempat `baseConfigurationReference` hanya menunjuk `Project.xcconfig` dan `App.xcconfig`.

### `F009-2` · Checkbox `derived` di halaman Actions

Dari laporan `chk-f009-verify` (2026-11-15). Membuktikan spec 0003 AC-10.

- **Prasyarat:** login GitHub dengan akses ke repo `ojiepermana/foundation-mobile`.
- **Jalankan:** buka `https://github.com/ojiepermana/foundation-mobile/actions/workflows/foundation.yml`, klik `Run workflow`, dan jangan klik tombol hijau.
- **Lulus bila:** checkbox `derived` ada dan tidak tercentang.
- **Hanya langkah ini yang bisa membuktikan:** form yang GitHub tampilkan. Bukti pengganti sudah lulus: definisi workflow di `main` memuat `inputs.derived` bertipe `boolean` dengan `default: false`, workflow aktif, dan run `43701289339` berjalan dengan input itu aktif.
