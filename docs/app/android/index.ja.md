# Openterface Android

## 概要

Openterface Mini-KVMは、Androidベースのインターフェースを通じてデバイスを制御するための基本的なKVM（キーボード、ビデオ、マウス）機能を提供するオープンソースのハードウェアおよびソフトウェアソリューションです。このリポジトリには、Androidアプリケーションのソースコード、ビルド設定、およびプロジェクトをセットアップして展開するためのサポートスクリプトが含まれています。

私たちはオープンハードウェアとオープンソースソフトウェアにコミットしており、[GNU Affero General Public License v3](LICENSE)の下でライセンスされています。

## 機能モジュール

### 1. ビデオ表示

#### 主な機能

-   接続されたターゲットデバイスからAndroid画面にリアルタイムでビデオ出力をストリーミングします。
-   最適な視聴のための画像調整をサポートします。

![image](https://assets.openterface.com/images/android/videoConnect.webp)

#### ユーザーインターフェースの説明

-   メイン画面にはターゲットデバイスのビデオフィードが表示され、インターフェースの大部分を占めます。
-   サイドにあるツールバーには調整コントロール（明るさ、コントラスト、色合い）が用意されています。

#### 操作フロー

1. Mini-KVMハードウェアをHDMIとUSBを介してターゲットデバイスに接続します。
2. Mini-KVMをUSB-Cを介してAndroidデバイスに接続します。
3. アプリを起動すると、ビデオフィードが自動的に表示されます。
4. ツールバーのスライダーを使って、明るさ、コントラスト、または色合いを調整します。

![image](https://assets.openterface.com/images/android/colorSetting.webp)

#### 特徴

-   ピンチでのズーム機能により、表示がより良くなります。

![image](https://assets.openterface.com/images/android/enlargeAndSideBar.webp)

---

### 2. マウスコントロール

#### 主な機能

-   ターゲットデバイスのインターフェースと対話するための絶対的および相対的なマウスコントロールを提供します。
-   左クリックと右クリックをサポートします。
-   右メニューからモードを選択します。

#### ユーザーインターフェースの説明

-   ビデオフィードはマウス入力用のタッチパッドとしても機能します。
-   フローティングアクションボタン（FAB）でマウスとキーボードモードを切り替えます。

#### 操作フロー

1. デバイスが正常に接続されていることを確認します。
2. 画面をタップして、その位置にマウスカーソルを移動させます（絶対コントロール）。
3. 一指でダブルクリックして左クリック、二指でクリックして右クリックします。
4. ドラッグモードは、左ボタンを押し続けることです。

#### 特徴

-   相対マウスコントロール（開発中、設定でトグル可能）。

## ![image](https://assets.openterface.com/images/android/mouseThouchMode.webp)

### 3. キーボード入力

#### 主な機能

-   キーボードのキーをクリックしてデバイスに入力します。

#### ユーザーインターフェースの説明

-   キーボードアイコンは右下隅にあります。
-   キーボードにはショートカットキー、システムキー、標準キー、ファンクションキー（F1-F12）が含まれています。

#### 操作フロー

1. 右下隅のキーボードアイコンをクリックしてキーボードを表示します。
2. 必要に応じてテキストを入力したり、ファンクションキーを押します。

#### 特徴やショートカット

-   **ショートカットキー**: Ctrl+C、Ctrl+V、Ctrl+Z、Ctrl+X、Ctrl+A、Ctrl+S、
    Win+Tab、Win+S、Win+E、Win+R、Win+D、Win+L、Alt+F4、Ctrl+Alt+Del、Alt+PrtScr。
-   **ファンクションキー**: F1-F12、記号キー。
-   **標準キー**: 0-9、A-Z、Enter、Space、Delete。

![image](https://assets.openterface.com/images/android/enlargeAndKeyBoard.webp)
![image](https://assets.openterface.com/images/android/keyBoardFunction.webp)
![image](https://assets.openterface.com/images/android/keyBoardSystem.webp)

---

その間、最新のコード、アップデート、例を探したり、問題を報告するために、オープンソースの**GitHubリポジトリ**: [Openterface_Android](https://github.com/TechxArtisanStudio/Openterface_Android)を自由に探索してください。

また、私たちの[Discordコミュニティ](/discord)に参加して、開発チームや他の素晴らしいユーザーとつながり、KVMに関連するトピックについて話し合うこともできます。

直接サポートが必要な場合は、[support@openterface.com](mailto:support@openterface.com)までお気軽にメールしてください。

---

**このページについてのフィードバックがありますか？** [こちらでお知らせください。](https://forms.gle/wmxoR2C1VdG36mT69)