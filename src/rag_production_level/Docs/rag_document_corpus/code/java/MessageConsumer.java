package com.nexus.messaging;

public final class MessageConsumer {
    private final MetadataService service;
    private final DeadLetterPublisher deadLetterPublisher;

    public MessageConsumer(MetadataService service,
                           DeadLetterPublisher deadLetterPublisher) {
        this.service = service;
        this.deadLetterPublisher = deadLetterPublisher;
    }

    public void consume(MetadataRequest request) {
        try {
            service.process(request);
        } catch (UnsupportedFormatException | MalformedDocumentException ex) {
            deadLetterPublisher.publishPermanentFailure(request, ex.getMessage());
        } catch (RuntimeException ex) {
            throw ex; // broker retry policy handles transient failures
        }
    }
}
