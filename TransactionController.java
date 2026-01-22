
@RestController
@RequestMapping("/transactions")
public class TransactionController {
    @PostMapping
    public String submit() {
        return "Sent to Kafka";
    }
}
