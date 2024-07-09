# Features

## Text Transfer 📝

=== "Users"

    - **Using Text Transfer**: The text transfer functionality allows you to send text from the host computer to the target device. This feature emulates typing behaviour to reproduce text content on the target computer.

    - **Special Characters**: The text transfer feature supports various ASCII characters, including symbols, punctuation marks, and non-alphanumeric characters.

    - **Limited Text**: It is ideal to transfer a short test like username, long password, code snippets from the host to the target. You can transfer text of varying lengths, but it is not recommended to transfer too much text at one time to avoid potential issues.

    !!! warning "Limitations of Text Transfer Feature"

        - **No Clipboard Integration**: The text transfer feature is designed to emulate typing behaviour and cannot transfer non-textual content, such as images or formatted text.
        - **Language Limitations**: This feature exclusively supports transferring text based on ASCII codes and does not support languages that are not ASCII-based, such as Chinese, Japanese, or Korean characters.

=== "🛠️ Test & Dev"

    - **Functionality Testing**: Verify that the host application can successfully transfer text from the host computer to the target device using ASCII codes.

    - **Content Integrity**: Ensure the text content transferred from the host to the target device remains intact and is accurately reproduced.

    - **Special Characters Handling**: Test the text transfer feature with various ASCII characters to ensure proper handling and reproduction on the target device.

    - **Text Length Testing**: Test the text transfer feature with text of varying lengths to verify that it can accommodate different text sizes without issues.

    - **Error Handling**: Test error scenarios, such as loss of connection or interruption during text transfer, to ensure the host application handles these situations gracefully and provides appropriate feedback to the user.

    - **Performance Testing**: Evaluate the performance of the text transfer feature under various conditions, including on older or slower computers, to identify any potential issues with mis-receiving HID input signals and ensure smooth operation.

    - **User Interface Testing**: Ensure the user interface of the host application provides intuitive controls and feedback for initiating and monitoring text transfer operations, making it easy for users to understand and use this feature effectively.

## More to Come

We have a [roadmap](/roadmap) page detailing our plans for developing more advanced features. Check it out to stay updated on what's coming next. We also welcome developers to join us and hang out in our [community](/community)!