---
draft: false
date: 2024-05-31
description: "MAKE: MagazineのDavid Groomとのライブストリームをご覧ください。Openterface Mini-KVMの起源ストーリーについて、テックアートプロジェクトからコミュニティ主導の開発、そしてヘッドレスデバイス管理のためのオープンソースソリューション作成の旅路について議論しました。"
keywords: "Openterface Mini-KVM, MAKE Magazine, David Groom, テックアートプロジェクト, オープンソースハードウェア, ヘッドレスコンピューター制御, Raspberry Pi管理, TechxArtisanスタジオ, メーカーコミュニティ, クラウドファンディングキャンペーン, DIYエレクトロニクス, ハードウェア開発, ライブストリームインタビュー"
---

# MAKE: MagazineのDavid Groomとのカジュアルチャット：Openterface Mini-KVMのストーリー

皆さん、こんにちは！

MAKE: MagazineのDavid Groomとの素晴らしい[YouTubeライブストリーム](https://www.youtube.com/live/lwitzvmxsgc?si=s9a1t5_Sce5v22e1)が終了しました！セッション中、私たちはOpenterface Mini-KVMの背景にあるストーリーについて深く掘り下げました。これは、ノートパソコンだけでRaspberry Piのようなヘッドレスデバイスやシングルボードコンピューターを簡単に制御するために設計された革新的なオープンソースハードウェアソリューションです。詳細についてはYouTubeライブストリームをご確認いただくか、下記のストーリーをお読みください。

![youtube-with-david-2](https://www.crowdsupply.com/img/2b83/081f1376-b266-4e83-b1af-5628dbe62b83/youtube-with-david_jpg_gallery-lg.jpg)

## アイデアの誕生

Mini-KVMの旅路は、中国の広州の賑やかな街のTechxArtisanスタジオで始まりました。過去5年間、私たちは地元および国際的なアーティストのための数多くのテックアートプロジェクトに深く関わってきました。私たちの仕事には、AI検出を備えたインタラクティブな照明インスタレーションの構築、劇場パフォーマンス用のロボットアーム、ランダムな迷路を解く自動運転ミニカー、さらには砂漠や森林などの無人地帯を探索するために設計されたロボット犬も含まれます。

![techxartisan_tech_art](https://www.crowdsupply.com/img/bce8/9c580077-993a-42b2-b781-a30d34acbce8/techxartisan-tech-art_jpg_gallery-lg.jpg)

### 共通の悩み
私たちの仕事で繰り返し発生する課題は、Raspberry PiやJetson Nanoのような多数のヘッドレスコンピューターの管理でした。これらはモニター、キーボード、またはネットワーク接続を欠いており、過酷な条件でこれらのデバイスをトラブルシューティングしてアクセスするために、予備のモニターやキーボードを必死に探すことがよくありました。

### 応急処置のソリューション
当初、私たちはバッテリーパックで動作し、タッチパッド付きのワイヤレスミニキーボードを組み合わせた応急処置のポータブルモニターソリューションに頼っていました。しかし、これらはしばしば忘れられたり置き忘れられたりするため、コーディングとセットアップのために常に携帯していたノートパソコンを活用できる専用ハードウェアソリューションの必要性が生じました。

![diy-monitor-keyboard](https://www.crowdsupply.com/img/2efd/4459eff9-2d01-4552-ac91-a1941ed82efd/diy-monitor-keyboard_jpg_gallery-lg.jpg)
*現場プロジェクトでは、この2つのガジェットを携帯する必要があります。*

### 最初のプロトタイプ
私たちの最初のDIYプロトタイプは、ヘッドレスデバイスからビデオを取得するためのキャプチャカードとUSBキーボード/マウスシミュレーターの組み合わせで、シンプルでありながら効果的でした。これらすべてがノートパソコンに接続する単一のUSBケーブルに統合されていました。

![/early-mini-kvm-pcb](https://www.crowdsupply.com/img/1f7e/fb91d879-dee7-45cc-bbdc-dc3ea5731f7e/early-mini-kvm-pcb_jpg_gallery-lg.jpg)
*mini-KVM PCBの初期バージョンの一つ*

2023年11月の深圳メーカーフェアで私たちのクールなテックアートプロジェクトを展示し、Davidにmini-KVMプロトタイプを見せるつもりでした。しかし、Davidからのギフトに興奮しすぎて、それを忘れてしまいました！

![techxartisan_team_with_david_groom](https://www.crowdsupply.com/img/bc4e/17bdcc6e-0a34-4f2f-bf64-fee0b8d6bc4e/techxartisan-team-with-david-groom_jpg_gallery-lg.jpg)
*MAKE: Magazineのステッカーとポストカードは本当にクールです！*

## コミュニティフィードバックと開発
Redditでプロトタイプを共有した後、[コミュニティ](/community/)から貴重なフィードバックを受け取り、ソリューションを洗練させ、完成した製品に開発するよう励まされました。このコミュニティサポートは、私たちの応急処置デバイスをホームラバー、システム管理者、テック愛好家、そしてヘッドレスコンピューターを扱うすべての人にとっての洗練された効率的なツールに変えるのに不可欠でした。

![got_feedback_from_reddit](https://www.crowdsupply.com/img/b24b/e04dfa15-1e5b-4bfb-b97c-acdba784b24b/got-feedback-from-reddit_jpg_gallery-lg.jpg)
*ホームラバーから大量のフィードバックを受け取りました*

## 疑念の克服
既存の類似ソリューションとの競争に対する最初の疑念にもかかわらず、オンラインコミュニティからの積極的な反応と建設的な提案は、潜在的なユースケースを明確にし、私たちの自信を高めました。このサポートと私たちの努力への肯定がなければ、プロジェクトをさらに進めることはなかったかもしれません。

## クラウドファンディングと将来の計画
Crowd SupplyでのOpenterface Mini-KVMのクラウドファンディングキャンペーンは本格的に勢いを増しており、あと約2週間で終了します。このキャンペーンは単にMini-KVMを開発するだけではありません。コミュニティ主導のイノベーションの力を証明するものです。次に、生産管理、ソフトウェア改善、そしてこの便利なガジェットを素晴らしいバッカーに届けることに取り組みます——すべて私たちの素晴らしいオープンソースコミュニティによって推進されています。

![techxartisan_openterface_discord](https://www.crowdsupply.com/img/8d7a/58e213e7-7a81-47b4-9d6b-69be3c698d7a/techxartisan-openterface-discord_jpg_gallery-lg.jpg)
*ベータテスターがTechxArtisanのDiscordで日常のテックタスクでのOpenterface Mini-KVMの使用を共有しています*

## オープンソースビジョンの受け入れ

Openterface Mini-KVMは私たちの創造性と忍耐力、そして支援的なオープンソースコミュニティの証です。私たちの個人的な課題に対するシンプルなソリューションとして始まったものが、世界中のハッカー、ティンカラー、テック愛好家に利益をもたらす多機能なオープンソースツールに進化しました。Mini-KVMが正式リリースに近づくにつれて、さらなるアップデートをお楽しみに！
